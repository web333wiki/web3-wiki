#!/usr/bin/env python3
"""
Auto Internal Links Script for Web3 Wiki

This script automatically generates and manages internal links in markdown cards using Obsidian-style linking.

Workflow:
1. Generate content manually without worrying about internal links
2. Run this script to:
   a. Generate card_index.txt from existing cards
   b. Remove all existing internal links from cards
   c. Process all cards and add appropriate internal links based on current card index

Test Cases:
The script includes comprehensive test cases in the test-cases/ folder:
- test-cases/test-card.md: Input markdown with various scenarios
- test-cases/test-card-index.txt: Simulated card index for testing
- test-cases/test-card-expected.md: Expected output after processing

Internal Link Rules:
1. Format: Use Obsidian-style [[card_name]] and [[card_name|display_name]]
2. Display Names: When a card name appears mid-sentence, use display_name to maintain readability
   (e.g., "The [[Proof of stake|proof of stake]] consensus" instead of "The [[Proof of stake]] consensus")
3. Clean Slate Approach: Remove all existing internal links first, then re-add them based on current card index
4. Heading Exclusion: Never add internal links within markdown headings
5. External Link Preservation: Keep existing external links unchanged
6. One Link Per Card: Each term is linked only once per card, at its first occurrence
7. Case Sensitivity: Match terms case-insensitively but preserve original casing in display names
8. Context Awareness: Avoid linking in code blocks, tables headers, and other inappropriate contexts
"""

import re
import os
from pathlib import Path
from typing import Set, Dict, List, Tuple
import sys


class AutoLinker:
    def __init__(self, card_index_path: str):
        """Initialize with card index file path."""
        self.card_index_path = card_index_path
        self.cards = self._load_card_index()
        self.linked_terms = {}  # Track which terms have been linked in each document
        
    def _load_card_index(self) -> Set[str]:
        """Load card names from index file."""
        cards = set()
        if os.path.exists(self.card_index_path):
            with open(self.card_index_path, 'r', encoding='utf-8') as f:
                for line in f:
                    card = line.strip()
                    if card:
                        cards.add(card)
        return cards

    def _is_in_code_block(self, content: str, position: int) -> bool:
        """Check if position is within a code block."""
        # Count code block markers before position
        before = content[:position]
        code_fence_count = before.count('```')
        return code_fence_count % 2 == 1
    
    def _is_in_inline_code(self, content: str, position: int) -> bool:
        """Check if position is within inline code."""
        # Find all inline code spans
        for match in re.finditer(r'`[^`]+`', content):
            if match.start() <= position <= match.end():
                return True
        return False
    
    def _is_in_heading(self, line: str) -> bool:
        """Check if the line is a markdown heading."""
        return bool(re.match(r'^#{1,6}\s', line))
    
    def _is_in_external_link(self, content: str, position: int) -> bool:
        """Check if position is within an external markdown link."""
        # Find all external links [text](url)
        for match in re.finditer(r'\[[^\]]+\]\([^)]+\)', content):
            if match.start() <= position <= match.end():
                return True
        return False

    def _remove_all_internal_links(self, content: str) -> str:
        """Remove all internal links and keep only the display text."""
        # Pattern to match internal links [[card]] or [[card|display]]
        pattern = re.compile(r'\[\[([^\]|]+)(?:\|([^\]]+))?\]\]')
        
        def replace_link(match):
            card_name = match.group(1)
            display_name = match.group(2)
            # Return display name if exists, otherwise return card name
            return display_name if display_name else card_name
        
        return pattern.sub(replace_link, content)

    def _add_internal_links(self, content: str) -> str:
        """Add internal links to content where appropriate."""
        # Find all code blocks first to skip them
        code_blocks = []
        for match in re.finditer(r'```[\s\S]*?```', content):
            code_blocks.append((match.start(), match.end()))
        
        lines = content.split('\n')
        result_lines = []
        linked_terms = {}  # Track what's been linked globally across the entire document
        
        for line_idx, line in enumerate(lines):
            # Skip headings
            if self._is_in_heading(line):
                result_lines.append(line)
                continue
            
            # Calculate line offset for code block checking
            line_offset = sum(len(lines[i]) + 1 for i in range(line_idx))
            
            # Check if this is a list item or table row
            is_list_item = bool(re.match(r'^\s*[-*+]\s', line))
            is_table_row = '|' in line
            
            # Check if we're in a table header
            is_table_header = False
            if is_table_row and line_idx + 1 < len(lines):
                next_line = lines[line_idx + 1]
                if re.match(r'^\s*\|[\s\-:]+\|', next_line):
                    is_table_header = True
            
            # Collect all potential matches for this line
            all_matches = []
            terms_in_this_line = set()  # Track what's already matched in this line
            
            for card in self.cards:
                card_lower = card.lower()
                
                # Skip if this term has already been linked anywhere in the document
                if card_lower in linked_terms:
                    continue
                
                # Skip if already found in this line
                if card_lower in terms_in_this_line:
                    continue
                
                # Create patterns for both singular and plural forms
                patterns = []
                patterns.append((card, re.compile(r'\b(' + re.escape(card) + r')\b(?!-)', re.IGNORECASE)))
                if not card.endswith('s'):
                    plural_pattern = re.compile(r'\b(' + re.escape(card) + r's)\b(?!-)', re.IGNORECASE)
                    patterns.append((card, plural_pattern))
                
                for original_card, pattern in patterns:
                    matches = list(pattern.finditer(line))
                    if not matches:
                        continue
                        
                    # Only process first match for lists/tables
                    match = matches[0]
                    match_start = match.start()
                    match_text = match.group(1)
                    absolute_pos = line_offset + match_start
                    
                    # Skip if in code block
                    in_code = False
                    for cb_start, cb_end in code_blocks:
                        if cb_start <= absolute_pos < cb_end:
                            in_code = True
                            break
                    if in_code:
                        continue
                    
                    # Skip if in inline code or external link
                    if (self._is_in_inline_code(line, match_start) or
                        self._is_in_external_link(line, match_start)):
                        continue
                    
                    # Skip table headers
                    if is_table_header:
                        continue
                    
                    all_matches.append({
                        'card': original_card,
                        'start': match_start,
                        'end': match_start + len(match_text),
                        'text': match_text,
                        'card_lower': card_lower,
                        'length': len(card)
                    })
                    
                    # Mark as found in this line
                    terms_in_this_line.add(card_lower)
                    break  # Only first match
            
            # Sort by position and card length (longer first to handle overlaps)
            all_matches.sort(key=lambda x: (x['start'], -x['length']))
            
            # Remove overlapping matches
            non_overlapping = []
            used_positions = set()
            
            for match in all_matches:
                # Check if this position overlaps with any already used
                positions = set(range(match['start'], match['end']))
                if not positions.intersection(used_positions):
                    non_overlapping.append(match)
                    used_positions.update(positions)
                    
                    # Mark as linked globally across the document
                    linked_terms[match['card_lower']] = True
            
            # Apply replacements in reverse order
            non_overlapping.sort(key=lambda x: x['start'], reverse=True)
            working_line = line
            
            for match in non_overlapping:
                card = match['card']
                text = match['text']
                
                # Use display name if text differs from card
                if text != card:
                    replacement = f'[[{card}|{text}]]'
                else:
                    replacement = f'[[{card}]]'
                
                working_line = (working_line[:match['start']] + 
                              replacement + 
                              working_line[match['end']:])
            
            result_lines.append(working_line)
        
        return '\n'.join(result_lines)

    def process_content(self, content: str) -> str:
        """Process markdown content to add internal links after removing all existing ones."""
        # First, remove ALL internal links to start with a clean slate
        content = self._remove_all_internal_links(content)
        
        # Then add new internal links
        content = self._add_internal_links(content)
        
        return content


def generate_card_index(cards_dir: str, output_file: str):
    """Generate card index from markdown files in cards directory."""
    cards = []
    cards_path = Path(cards_dir)
    
    if cards_path.exists():
        for md_file in cards_path.glob('*.md'):
            # Remove .md extension
            card_name = md_file.stem
            cards.append(card_name)
    
    # Sort cards alphabetically
    cards.sort()
    
    # Write to index file
    with open(output_file, 'w', encoding='utf-8') as f:
        for card in cards:
            f.write(card + '\n')
    
    print(f"Generated card index with {len(cards)} cards")


def process_markdown_file(file_path: str, linker: AutoLinker) -> bool:
    """Process a single markdown file to add internal links."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Process content
        new_content = linker.process_content(content)
        
        # Only write if content changed
        if new_content != content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            return True
        return False
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return False


def run_tests():
    """Run test cases to verify the script works correctly."""
    print("Running tests...")
    
    # Test with the provided test files
    test_dir = Path(__file__).parent / 'test-cases'
    test_input = test_dir / 'test-card.md'
    test_index = test_dir / 'test-card-index.txt'
    test_expected = test_dir / 'test-card-expected.md'
    test_output = test_dir / 'test-output.md'
    
    if not all([test_input.exists(), test_index.exists(), test_expected.exists()]):
        print("Test files not found!")
        return False
    
    # Initialize linker with test index
    linker = AutoLinker(str(test_index))
    
    # Read test input
    with open(test_input, 'r', encoding='utf-8') as f:
        input_content = f.read()
    
    # Process content
    output_content = linker.process_content(input_content)
    
    # Write output for inspection
    with open(test_output, 'w', encoding='utf-8') as f:
        f.write(output_content)
    
    # Read expected output
    with open(test_expected, 'r', encoding='utf-8') as f:
        expected_content = f.read()
    
    # Compare
    if output_content == expected_content:
        print("✓ Tests passed!")
        return True
    else:
        print("✗ Tests failed!")
        print(f"Output written to {test_output}")
        print("Differences found - check the output file")
        return False


def main():
    """Main function to process all cards."""
    # Determine script location
    script_dir = Path(__file__).parent
    project_root = script_dir.parent.parent
    cards_dir = project_root / 'cards'
    card_index_file = script_dir / 'card_index.txt'
    
    # Check if running tests
    if len(sys.argv) > 1 and sys.argv[1] == 'test':
        success = run_tests()
        sys.exit(0 if success else 1)
    
    # Generate card index
    print("Generating card index...")
    generate_card_index(str(cards_dir), str(card_index_file))
    
    # Initialize linker
    linker = AutoLinker(str(card_index_file))
    
    # Process all markdown files in cards directory
    print("\nProcessing cards...")
    processed = 0
    updated = 0
    
    for md_file in cards_dir.glob('*.md'):
        processed += 1
        if process_markdown_file(str(md_file), linker):
            updated += 1
            print(f"  Updated: {md_file.name}")
    
    print(f"\nProcessed {processed} cards, updated {updated} cards")


if __name__ == '__main__':
    main()



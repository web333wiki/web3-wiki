#!/usr/bin/env python3
"""
check-internal-links.py - Generate a card index and verify internal wiki links

This script performs two main functions:
1. Generate an index of all Markdown cards in the cards directory
2. Check for broken internal links across all cards

The script exits with a non-zero status code if any broken links are found,
making it suitable for CI/CD pipelines.
"""

import os
import re
import sys
from typing import Dict, List, Optional, Set, Tuple, Pattern


# Constants
CARDS_DIR = 'cards'
CARD_INDEX_FILE = 'scripts/card_index.txt'

# Type aliases for clarity
CardName = str
LineNumber = int
LinkTarget = str
BrokenLink = Tuple[CardName, LineNumber, LinkTarget]


def validate_cards_directory() -> bool:
    if not os.path.isdir(CARDS_DIR):
        print(f"Error: Cards directory '{CARDS_DIR}' not found.", file=sys.stderr)
        return False
    return True


def generate_card_index() -> List[str]:
    card_names = []
    
    for filename in os.listdir(CARDS_DIR):
        if filename.endswith(".md"):
            card_name = os.path.splitext(filename)[0]
            card_names.append(card_name)
    
    # Sort for consistency
    card_names.sort()
    
    # Write the index file
    try:
        with open(CARD_INDEX_FILE, "w", encoding='utf-8') as f:
            for name in card_names:
                f.write(f"{name}\n")
        print(f"Successfully generated '{CARD_INDEX_FILE}' with {len(card_names)} card names.")
    except IOError as e:
        print(f"Error writing to '{CARD_INDEX_FILE}': {e}", file=sys.stderr)
        sys.exit(1)
        
    return card_names


def find_broken_links(card_names: List[str]) -> List[BrokenLink]:
    valid_cards = set(card_names)
    
    if not valid_cards:
        print(f"Info: No cards were indexed from '{CARDS_DIR}'. Nothing to check for links.")
        return []
    
    # Regex to match Obsidian-style internal links: [[Link Name]] or [[Link Name|Alias]]
    link_pattern = re.compile(r'\[\[([^\|\]]+)(?:\|[^\]]*?)?\]\]')
    
    broken_links = []
    files_processed = 0
    
    for filename in os.listdir(CARDS_DIR):
        if not filename.endswith('.md'):
            continue
            
        files_processed += 1
        file_path = os.path.join(CARDS_DIR, filename)
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                for line_num, line in enumerate(f, 1):
                    for match in link_pattern.finditer(line):
                        link_target = match.group(1).strip()
                        
                        # Handle section anchors (e.g., [[Card Name#Section]])
                        base_card_name = link_target.split('#')[0]
                        
                        if base_card_name not in valid_cards:
                            broken_links.append((filename, line_num, link_target))
        except FileNotFoundError:
            print(f"Warning: File {filename} disappeared during processing.", file=sys.stderr)
        except Exception as e:
            print(f"Error reading file {filename}: {e}", file=sys.stderr)
    
    # Handle edge case where files were removed between indexing and link checking
    if not files_processed and card_names:
        print("Warning: Cards were indexed, but no markdown files found during link checking. Files may have been deleted.")
    
    return broken_links


def report_broken_links(broken_links: List[BrokenLink]) -> bool:
    if not broken_links:
        print("All internal links are valid.")
        return True
        
    # Report each broken link
    for card, line_num, link in broken_links:
        print(f"Broken link in {card} (line {line_num}): [[{link}]]")
    
    print(f"\nERROR: {len(broken_links)} broken internal link(s) found.")
    return False


def main() -> int:
    # Validate cards directory
    if not validate_cards_directory():
        return 1
    
    # Generate card index
    card_names = generate_card_index()
    
    # Find broken links
    broken_links = find_broken_links(card_names)
    
    # Report findings and determine exit status
    if not report_broken_links(broken_links):
        return 1
        
    return 0


if __name__ == "__main__":
    sys.exit(main()) 
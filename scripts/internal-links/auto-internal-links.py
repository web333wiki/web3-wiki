#!/usr/bin/env python3
"""
Auto Internal Links Script for Web3 Wiki

This script automatically generates and manages internal links in markdown cards using Obsidian-style linking.

Workflow:
1. Generate content manually without worrying about internal links
2. Run this script to:
   a. Generate card_index.txt from existing cards
   b. Process all cards and add appropriate internal links
   c. Validate and clean up existing internal links

Test Cases:
The script includes comprehensive test cases using:
- test-card.md: Input markdown with various scenarios
- test-card-index.txt: Simulated card index for testing
- test-card-expected.md: Expected output after processing

Internal Link Rules:
1. Format: Use Obsidian-style [[card_name]] and [[card_name|display_name]]
2. Display Names: When a card name appears mid-sentence, use display_name to maintain readability
   (e.g., "The [[Proof of stake|proof of stake]] consensus" instead of "The [[Proof of stake]] consensus")
3. Validation: Check existing internal links against card_index.txt
   - If valid but needs display name formatting, update it
   - If invalid (card doesn't exist), remove the link
4. Heading Exclusion: Never add internal links within markdown headings
5. External Link Preservation: Keep existing external links unchanged
6. First Occurrence Only: For multiple instances of the same potential link, only link the first occurrence
7. Case Sensitivity: Match terms case-insensitively but preserve original casing in display names
8. Context Awareness: Avoid linking in code blocks, tables headers, and other inappropriate contexts
"""



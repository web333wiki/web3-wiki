#!/usr/bin/env python3
"""
check-tag.py - Validate category tags in card files

This script ensures that all card files have the correct category tags:
1. Each card must have exactly one valid category tag as the first line
2. Valid tags are: #show-card, #awesome-card, #explain-card
3. Exception: Web3 Wiki.md (main page) should contain all valid tags

The script exits with a non-zero status code if any invalid tags are found.
"""

import os
import sys
from pathlib import Path
from typing import List, Set


# Constants
CARDS_DIR = 'cards'
VALID_TAGS = {'#show-card', '#awesome-card', '#explain-card'}
MAIN_PAGE_FILE = 'Web3 Wiki.md'


def validate_cards_directory() -> bool:
    """Check if the cards directory exists."""
    if not os.path.isdir(CARDS_DIR):
        print(f"Error: Cards directory '{CARDS_DIR}' not found.", file=sys.stderr)
        return False
    return True


def check_main_page_tags(file_path: str, lines: List[str]) -> bool:
    """
    Check if the main page contains all valid tags in the first line.
    
    Args:
        file_path: Path to the file being checked
        lines: List of lines from the file
        
    Returns:
        True if valid, False otherwise
    """
    if not lines:
        print(f"Error: {MAIN_PAGE_FILE} is empty.", file=sys.stderr)
        return False
    
    first_line = lines[0].strip()
    
    # Check if all valid tags are present in the first line
    missing_tags = []
    for tag in VALID_TAGS:
        if tag not in first_line:
            missing_tags.append(tag)
    
    if missing_tags:
        print(f"Error: {MAIN_PAGE_FILE} is missing these tags in the first line: {', '.join(missing_tags)}")
        return False
    
    return True


def check_regular_card_tags(file_path: str, lines: List[str]) -> bool:
    """
    Check if a regular card has exactly one valid tag.
    
    Args:
        file_path: Path to the file being checked
        lines: List of lines from the file
        
    Returns:
        True if valid, False otherwise
    """
    if not lines:
        print(f"Error: {file_path} is empty and does not contain a category tag.")
        return False
    
    first_line = lines[0].strip()
    
    # Check if the first line contains exactly one valid tag
    tags_in_first_line = [tag for tag in VALID_TAGS if tag in first_line]
    
    if len(tags_in_first_line) == 0:
        print(f"Error: {file_path} does not have a valid category tag as the first line.")
        print(f"       First line: '{first_line}'")
        print(f"       Expected one of: {', '.join(sorted(VALID_TAGS))}")
        return False
    
    if len(tags_in_first_line) > 1:
        print(f"Error: {file_path} has multiple category tags in the first line: {', '.join(tags_in_first_line)}")
        return False
    
    # Check if the first line is exactly the tag (no extra content)
    expected_tag = tags_in_first_line[0]
    if first_line != expected_tag:
        print(f"Error: {file_path} first line should contain only the category tag.")
        print(f"       Found: '{first_line}'")
        print(f"       Expected: '{expected_tag}'")
        return False
    
    return True


def check_single_card(file_path: str) -> bool:
    """
    Check a single card file for valid category tags.
    
    Args:
        file_path: Path to the card file
        
    Returns:
        True if valid, False otherwise
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        filename = os.path.basename(file_path)
        
        if filename == MAIN_PAGE_FILE:
            return check_main_page_tags(file_path, lines)
        else:
            return check_regular_card_tags(file_path, lines)
            
    except FileNotFoundError:
        print(f"Error: File {file_path} not found.", file=sys.stderr)
        return False
    except Exception as e:
        print(f"Error reading file {file_path}: {e}", file=sys.stderr)
        return False


def check_all_cards() -> int:
    """
    Check all card files for valid category tags.
    
    Returns:
        0 if all cards are valid, 1 if any issues are found
    """
    if not validate_cards_directory():
        return 1
    
    invalid_cards = []
    total_cards = 0
    
    # Process all markdown files in the cards directory
    for root, _, files in os.walk(CARDS_DIR):
        for filename in files:
            if filename.endswith('.md'):
                total_cards += 1
                file_path = os.path.join(root, filename)
                
                if not check_single_card(file_path):
                    invalid_cards.append(filename)
    
    # Report results
    if not invalid_cards:
        print(f"All {total_cards} cards have valid category tags.")
        return 0
    else:
        print(f"\nFound {len(invalid_cards)} cards with invalid category tags:")
        for card in invalid_cards:
            print(f"- {card}")
        return 1


if __name__ == "__main__":
    sys.exit(check_all_cards())
#!/usr/bin/env python3
"""
check-card-name.py - Validate card filenames according to naming conventions

This script checks that card names follow these conventions:
1. No special characters, only letters, numbers, spaces
2. First letter is uppercase
3. Only the first word should be capitalized
4. Exceptions exist for specific patterns like ERC-20, EIP-*, BIP-*

The script exits with a non-zero status code if any invalid names are found.

Examples of valid names:
- Ethereum.md
- Smart contract.md
- Zero knowledge proof.md

Examples of invalid names:
- ethereum.md (first letter not uppercase)
- Ethereum (DeFi).md (contains special characters)
- ByBit's $1.4 Billion ETH Hack.md (contains special characters)
- Zero Knowledge Proof.md (words after first are capitalized)
"""

import os
import re
import sys

# Constants
CARDS_DIR = 'cards'

# Define patterns for exceptions
EXCEPTION_PATTERNS = [
    r'^ERC-\d+$',
    r'^EIP-\d+$',
    r'^BIP-\d+$',
    r'^zkKYC$',
    r'^The Merge$',
    r'^Web3 Wiki$',
]

def validate_cards_directory():
    if not os.path.isdir(CARDS_DIR):
        print(f"Error: Cards directory '{CARDS_DIR}' not found.", file=sys.stderr)
        return False
    return True

def is_exception(name):
    for pattern in EXCEPTION_PATTERNS:
        if re.match(pattern, name):
            return True
    return False

def validate_card_name(filename):
    # Remove .md extension
    name = os.path.splitext(filename)[0]
    
    # Check for exceptions first
    if is_exception(name):
        return True, None
    
    # Check if name contains only allowed characters (letters, numbers, spaces)
    if not re.match(r'^[A-Za-z0-9 ]+$', name):
        return False, f"Contains special characters other than letters, numbers, or spaces"
    
    # Check capitalization of first letter
    if not name[0].isupper():
        return False, f"First letter is not uppercase"
    
    # Check if other words start with uppercase
    words = name.split()
    for word in words[1:]:  # Skip first word
        if word[0].isupper():
            return False, f"Only the first word should start with uppercase"
    
    # Return success if all checks pass
    return True, None

def check_card_names():
    """
    Check all card names and report any issues.
    
    This function:
    1. Validates all card names in the cards directory
    2. Reports any invalid names with error messages
    3. Returns 0 if all names are valid, 1 otherwise
    """
    if not validate_cards_directory():
        return 1
    
    invalid_cards = []
    for filename in os.listdir(CARDS_DIR):
        if not filename.endswith('.md'):
            continue
    
        is_valid, error_message = validate_card_name(filename)
        if not is_valid:
            invalid_cards.append((filename, error_message))
    
    if not invalid_cards:
        print("All card names are valid.")
        return 0
    
    print(f"Found {len(invalid_cards)} cards with invalid names:")
    for filename, error in invalid_cards:
        print(f"- {filename}: {error}")
    
    return 1

if __name__ == "__main__":
    sys.exit(check_card_names()) 
import os
import sys

def check_cards():
    valid_tags = ['#show-card', '#awesome-card', '#explain-card']
    cards_dir = 'cards'

    for root, _, files in os.walk(cards_dir):
        for file in files:
            if file.endswith('.md'):
                with open(os.path.join(root, file), 'r') as f:
                    lines = f.readlines()
                    if not lines:
                        print(f"Error: {file} is empty and does not contain a category tag.")
                        sys.exit(1)
                    first_line = lines[0].strip()
                    if file == 'Web3 Wiki.md':
                        if not all(tag in first_line for tag in valid_tags):
                            print(f"Error: {file} does not contain all valid tags in the first line.")
                            sys.exit(1)
                    else:
                        tags_in_file = [line.strip() for line in lines if line.strip() in valid_tags]
                        if len(tags_in_file) != 1:
                            print(f"Error: {file} should contain exactly one valid tag.")
                            sys.exit(1)
    print("All cards are valid.")

if __name__ == "__main__":
    check_cards()
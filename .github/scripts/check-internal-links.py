import os
import re
import sys

CARDS_DIR = 'cards'

# Build a set of all valid card names (without .md extension)
valid_cards = set()
for file in os.listdir(CARDS_DIR):
    if file.endswith('.md'):
        valid_cards.add(file[:-3])  # Remove .md

# Regex to match Obsidian-style internal links: [[Link Name]] or [[Link Name|Alias]]
link_pattern = re.compile(r'\[\[([^\]|\n\]]+)(?:\|[^\]]*)?\]\]')

broken_links = []

for filename in os.listdir(CARDS_DIR):
    if not filename.endswith('.md'):
        continue
    path = os.path.join(CARDS_DIR, filename)
    with open(path, 'r', encoding='utf-8') as f:
        for i, line in enumerate(f, 1):
            for match in link_pattern.finditer(line):
                link_target = match.group(1).strip()
                # Obsidian links are case-sensitive and must match the filename (without .md)
                if link_target not in valid_cards:
                    broken_links.append((filename, i, link_target))

if broken_links:
    for card, line_num, link in broken_links:
        print(f"Broken link in {card} (line {line_num}): [[{link}]]")
    print(f"\nERROR: {len(broken_links)} broken internal link(s) found.")
    sys.exit(1)
else:
    print("All internal links are valid.") 
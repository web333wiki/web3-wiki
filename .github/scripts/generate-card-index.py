import os

def generate_card_index():
    cards_dir = "cards"
    output_file = ".github/card_index.txt"
    card_names = []

    if not os.path.isdir(cards_dir):
        print(f"Error: Directory '{cards_dir}' not found.")
        return

    for filename in os.listdir(cards_dir):
        if filename.endswith(".md"):
            card_names.append(os.path.splitext(filename)[0])

    with open(output_file, "w") as f:
        for name in sorted(card_names): # Sort the names for consistency
            f.write(name + "\n")

    print(f"Successfully generated '{output_file}' with {len(card_names)} card names.")

if __name__ == "__main__":
    generate_card_index() 
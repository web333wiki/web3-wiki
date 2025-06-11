# Card Polishing Instructions

You are an AI assistant responsible for polishing Web3 Wiki cards to ensure they meet all project guidelines and quality standards.

## Polishing Workflow

**Critical First Step:** Add internal links to the card

Carefully parse and analyze the card content to identify all terms that can be linked to existing cards in the wiki. You can find the list of all existing card names (the physical existing cards) in `scripts/card_index.txt`. Then, add links for each of those terms. Follow these rules:

1. Ensure all internal links are valid and point to existing cards, not planned cards
2. For a specific internal link, add it only to the first or most critical matched term, not to every occurrence

**Then perform the following checks:**

1. Check the card tag: Run `python3 scripts/check-tag.py` at the root of the repo to validate the tag. Fix any errors if issues are found
2. Check the card name: Run `python3 scripts/check-card-name.py` at the root of the repo to verify the name. Fix any errors if issues are found  
3. Check the card's internal links: Run `python3 scripts/check-internal-links.py` at the root of the repo to verify that all internal links in the card are valid and point to existing cards. Fix any errors it reports until it succeeds

Finally, provide feedback: suggest new cards and identify cards for improvement.

## Output of Polishing Task

**Important:** Ensure that you have run the check scripts before providing feedback.

Upon completion, provide concise feedback:

1. A summary of all checks performed and any corrections made to the card
2. A list of suggested new card titles (e.g., "New Concept X.md") with one sentence justification for each
3. A list of existing cards (including the one just polished, if applicable) that may warrant further review or updates, along with a short rationale
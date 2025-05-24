# Auto Internal Links Script

This script automatically manages internal links in markdown files for the Web3 Wiki project using Obsidian-style linking.

## Usage

### Generate card index and process all cards:

```bash
python3 auto-internal-links.py
```

### Run tests:

```bash
python3 auto-internal-links.py test
```

## Examples

Input:

```markdown
Bitcoin is a cryptocurrency. The bitcoin network uses proof of work.

- bitcoin is decentralized
- ethereum uses smart contracts
```

Output:

```markdown
[[Bitcoin]] is a cryptocurrency. The bitcoin network uses [[Proof of work|proof of work]].

- [[Bitcoin|bitcoin]] is decentralized
- [[Ethereum|ethereum]] uses [[Smart contract|smart contracts]]
```

## Test Cases

The script includes comprehensive test cases in the `test-cases/` folder:

- `test-cases/test-card.md`: Input with various scenarios
- `test-cases/test-card-expected.md`: Expected output
- `test-cases/test-card-index.txt`: Sample card index

Note: Some test cases include edge cases that may not reflect typical usage patterns.

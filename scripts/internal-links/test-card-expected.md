# Test Card

## Overview

This is a test card for testing internal links. It should link to [[Ethereum]] and [[Smart contract|smart contracts]] automatically. The card discusses various blockchain concepts like [[Bitcoin|bitcoin]], [[Solana|solana]], and [[Polygon|polygon]] networks. We also mention concepts like [[Decentralized finance|decentralized finance]] and [[Proof of stake|proof of stake]] consensus mechanisms.

## Existing Internal Links

This card already has some internal links: [[Ethereum]] and Invalid Link which doesn't exist. There's also [[Smart contract|smart contracts]] with display name that should be preserved.

## Markdown Headings

### Bitcoin Section
This heading contains Bitcoin but should not be linked.

### Ethereum Virtual Machine Analysis
This heading has Ethereum and EVM but neither should be linked.

The [[EVM]] is important for understanding how ethereum works. Here EVM should get a link, and the second mention of ethereum should not since Ethereum was already linked above.

## External Links Already Present

Check out [Ethereum](https://ethereum.org) official website. This should not be converted to internal link since it already has an external link.

Visit the [bitcoin whitepaper](https://bitcoin.org/bitcoin.pdf) for more details.

## Multiple Occurrences Test

The word ethereum appears multiple times. First occurrence should get link.
Second ethereum mention should not get a link.
Third Ethereum reference should also not get a link.

## Case Sensitivity Tests

We have ethereum in lowercase, Ethereum in proper case, and ETHEREUM in uppercase.
Testing ethereum virtual machine and EVM references.
The proof of stake mechanism works differently than [[Proof of work|proof of work]].

## Complex Scenarios

The proof of stake consensus mechanism is used by many networks. When we discuss proof of stake implementation, we need proper display names.

Different networks like polygon and solana use various consensus mechanisms.

## Code Blocks and Technical Content

```javascript
// This code mentions Ethereum but should not be linked
const ethereum = window.ethereum;
```

Inline code like `ethereum.request()` should also not be linked.

## Lists and Tables

- [[Bitcoin|bitcoin]] is a cryptocurrency  
- Ethereum enables [[Smart contract|smart contracts]]
- [[Solana|solana]] is fast and scalable
- [[Polygon|polygon]] is a [[Layer 2]] solution

| Network  | Type    | Uses Gas |
|----------|---------|----------|
| [[Bitcoin|bitcoin]]  | Layer 1 | No       |
| Ethereum | Layer 1 | Yes      |
| [[Polygon|polygon]]  | [[Layer 2]] | Yes      |

## Gas and Transaction Fees

Transaction fees on ethereum are paid in [[Wei|wei]], the smallest unit. The [[Gas price|gas price]] affects how quickly transactions are processed on the EVM.

## DeFi and Web3 Ecosystem

This paragraph contains [[Web3|web3]] technologies and various concepts like [[Oracle|oracle]] networks and [[DEX]] platforms. The decentralized finance ecosystem relies on smart contracts.

## Edge Cases

- Text with "ethereum" in quotes should be linked
- References to ([[Bitcoin|bitcoin]]) in parentheses should be linked  
- The word ethereum-based should not be linked (hyphenated)
- Multiple [[Oracle|oracle]] and oracle mentions for testing
- Testing [[DEX]] and [[DEX|dex]] case variations

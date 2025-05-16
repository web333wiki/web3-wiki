#show-card

## What is Revoke.cash?

[Revoke.cash](https://revoke.cash/) is a security tool in the [[Web3]] ecosystem that helps users manage and revoke token allowances (approvals) granted to different smart contracts and decentralized applications ([[DApp]]s). It provides a user-friendly interface for crypto users to monitor, control, and revoke permissions they have previously given to various protocols to spend their tokens.

## Understanding Token Approvals

In [[Ethereum]] and [[ERC-20]] compatible blockchains, when interacting with dApps and protocols like decentralized exchanges ([[DEX]]s), lending platforms, or [[NFT]] marketplaces, users often need to grant these applications permission to access and transfer tokens on their behalf. This is done through the `approve` function in the ERC-20 standard.

These approvals come in two forms:
- **Limited approvals**: Permission to spend up to a specific amount of tokens
- **Unlimited approvals**: Permission to spend an infinite amount of tokens (most common)

## Why Revoke.cash is Useful

### Security Risks of Unlimited Approvals

Many dApps request unlimited token approvals for user convenience, but this creates significant security risks:

1. **Vulnerability to exploits**: If a dApp you've approved is hacked or has a vulnerability, attackers could drain all approved tokens
2. **Smart contract risks**: Bugs or backdoors in approved contracts could lead to loss of funds
3. **Forgotten approvals**: Users often forget which dApps they've granted permissions to over time

### Benefits of Using Revoke.cash

- **Visibility**: See all active token approvals across multiple chains in one dashboard
- **Control**: Selectively revoke unnecessary or risky approvals
- **Security**: Reduce attack surface by managing approval permissions
- **Multi-chain support**: Works across Ethereum, Polygon, BSC, and many other EVM-compatible networks
- **Risk reduction**: Minimize potential losses from smart contract vulnerabilities

## Best Practices

1. Regularly audit and revoke unnecessary token approvals
2. Only approve the exact amount needed for a transaction when possible
3. Revoke approvals immediately after completing transactions with a [[DApp]]
4. Use [[Hardware wallet]]s for additional security when managing approvals

Revoke.cash has become an essential security tool for responsible Web3 users, helping to mitigate one of the most common yet overlooked security risks in the ecosystem.


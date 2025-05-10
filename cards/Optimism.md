#show-card

## Project Overview

Optimism (OP Mainnet) is a leading Layer 2 (L2) scaling solution for Ethereum, designed to offer faster transactions and lower fees while maintaining Ethereum's security. It utilizes Optimistic Rollup technology and is a core component of the envisioned Superchain ecosystem.

Its core purpose is to scale Ethereum by processing transactions off-chain and then batching them to the Ethereum mainnet. Key features include EVM equivalence (making it easy to deploy existing Ethereum dApps), the open-source [[Op Stack]] development framework, and a strong focus on public goods funding through Retroactive Public Goods Funding (RetroPGF).

For more details, visit the [official Optimism website](https://www.optimism.io/).

## Technical Details

- **Underlying Technology:** Optimism uses Optimistic Rollups. Transactions are executed on Optimism (L2), and data is posted to Ethereum (L1). It assumes transactions are valid unless challenged via a fault proof mechanism (previously fraud proof).
- **Architecture Overview:** Optimism's architecture is built upon the [[Op Stack]]. Key components include a sequencer (orders and executes transactions), a proposer (submits transaction batches to L1), and verifiers (can challenge the validity of L2 state roots submitted to L1).
- **Unique Selling Points:**
  - **EVM Equivalence:** High degree of compatibility with Ethereum, simplifying dApp migration.
  - **[[Op Stack]]:** The underlying open-source stack allows other projects (e.g., Base, Zora) to build their own L2s, fostering a broader ecosystem (the Superchain).
  - **Optimism Collective & Governance:** A two-house governance system (Token House and Citizens' House) aims for a balanced and sustainable approach to network development and funding.
  - **RetroPGF:** A novel mechanism for funding public goods that have already demonstrated impact.

## Use Cases

- **Scaling Ethereum dApps:** Many popular Ethereum dApps have deployed on Optimism to offer users lower fees and faster transactions, including DeFi protocols, NFT marketplaces, and gaming applications.
- **DeFi Ecosystem:** Hosts a vibrant DeFi ecosystem with decentralized exchanges, lending platforms, yield farming, and more.
- **NFTs:** Supports a growing NFT space with various marketplaces and projects.
- **Superchain Infrastructure:** Serves as a foundational L2 for the Superchain initiative, aiming for a network of interoperable L2s built on the OP Stack.

## Getting Started

- **How to use/access:** Users can interact with Optimism by adding the OP Mainnet network to EVM-compatible wallets (e.g., MetaMask) and using bridges like the official Optimism Bridge to transfer assets from Ethereum.
- **Official Resources:**
  - Website: [Optimism.io](https://www.optimism.io/)
  - Documentation: [Optimism Docs](https://docs.optimism.io/)
  - Bridge: [Optimism Bridge](https://app.optimism.io/bridge)
  - Block Explorer: [Optimism Etherscan](https://optimistic.etherscan.io/)
- **Community Channels:** Active communities on Discord, Twitter, and the Optimism Governance Forum.

## Related Links (Optional)

- [[Layer 2]]
- [[Rollup]]
- [[Op Stack]]

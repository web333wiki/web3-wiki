#show-card

## Overview

Ethereum is a decentralized, open-source blockchain platform that enables the creation and deployment of smart contracts and decentralized applications (dApps). Launched in 2015 by [[Vitalik Buterin]] and team, Ethereum introduced programmable [[Smart Contract]]s and pioneered the concept of a blockchain-based world computer. Its native cryptocurrency, Ether (ETH), is used for transaction fees, staking, and as a store of value. Ethereum's ongoing upgrades aim to make it the global settlement layer for decentralized finance and Web3 applications.

- **Problem Solved:** Enables trustless, programmable transactions and decentralized applications, addressing the limitations of Bitcoin's scripting and centralized platforms.
- **Value Proposition:** Most widely adopted smart contract platform, with a robust developer ecosystem and continuous innovation.
- **Official Website:** [Official Ethereum Website](https://ethereum.org)
- **Status:** Live, with major upgrades ongoing (latest: Pectra, 2025)

## Key Features

- **Smart Contracts:** Self-executing code enabling dApps, DeFi, NFTs, DAOs, and more.
- **Ethereum Virtual Machine ([[EVM]]):** Universal runtime for smart contracts, enabling cross-platform compatibility.
- **Account Abstraction:** (EIP-7702, Pectra) Allows EOAs to temporarily act as smart contracts, improving wallet UX and enabling features like transaction batching, gas sponsorship, and programmable recovery.
- **Staking:** Transitioned to [[Proof of stake]] consensus, allowing users to secure the network and earn rewards by staking ETH.
- **Scalability:** Supports Layer 2 solutions and rollups (see [[Rollup]]), with recent upgrades (Dencun, Pectra) doubling blob throughput and reducing L2 fees.
- **Upgradeable Protocol:** Frequent hard forks and EIPs, with a clear roadmap (The Merge, Dencun, Pectra, and beyond).

## Technology

- **Blockchain/Platform:** Standalone, with the EVM as its core engine.
- **Architecture:** Layered design with execution (EVM) and consensus (Beacon Chain) layers.
- **Core Mechanisms:**
  - **Consensus:** [[Proof of stake]] (since The Merge, 2022)
  - **Smart Accounts:** EIP-7702 (Pectra, 2025) brings account abstraction natively to EOAs.
  - **Blob Transactions:** Introduced in Dencun (2024), expanded in Pectra (2025) to improve L2 data availability and reduce costs.
- **Smart Contracts:** Open source, with many audited contracts (see [[Awesome Ethereum]] for resources).

## Ecosystem & Use Cases

- **Target Audience:** Developers, DeFi users, NFT collectors, DAOs, enterprises, and general users.
- **How It's Used:**
  - Deploying dApps (DeFi, NFTs, DAOs, gaming, identity, etc.)
  - Staking and running validators (see [[Staking]], [[Validator]])
  - Interacting with L2s and rollups for scalable applications
- **Integrations:** Major L2s (Optimism, Arbitrum, Linea), wallets (MetaMask, hardware wallets), infrastructure (Infura, Alchemy), and more.
- **Tokenomics:**
  - **ETH Utility:** Gas, staking, collateral, governance, and more.
  - **Supply:** No fixed cap; supply is dynamic, with EIP-1559 introducing fee burning.
  - **See also:** [[Awesome Ethereum]] for more on tokens and DeFi.

## Getting Started & Resources

- **Access:** Use via web wallets (e.g., MetaMask), hardware wallets, or by running a node.
- **Documentation:** [Ethereum Docs](https://ethereum.org/en/developers/docs/)
- **Community:** [Ethereum Discord](https://discord.com/invite/CetY6Y4), [r/ethereum](https://reddit.com/r/ethereum), [@ethereum](https://twitter.com/ethereum)
- **Support:** [Ethereum Support](https://support.ethereum.org/)
- **Source Code:** [Ethereum GitHub](https://github.com/ethereum)

## Related Concepts

- [[EVM]]
- [[Smart Contract]]
- [[Proof of stake]]
- [[Rollup]]
- [[Staking]]
- [[Validator]]
- [[Vitalik Buterin]]
- [[Awesome Ethereum]]

## Latest Updates

- **2025:** Pectra upgrade activated, introducing EIP-7702 (account abstraction for EOAs), increased validator max stake (2048 ETH), doubled blob throughput, and more. [Pectra Mainnet Announcement](https://blog.ethereum.org/2025/04/23/pectra-mainnet)
- **2024:** Dencun upgrade introduced proto-danksharding (EIP-4844), enabling blob transactions and reducing L2 costs.
- **2022:** The Merge transitioned Ethereum from Proof-of-Work to Proof-of-Stake, reducing energy consumption by ~99.95%.
- **2021:** London upgrade (EIP-1559) introduced fee burning and improved transaction fee predictability.
- **2015:** Genesis block created, marking the official launch.
- **2013:** Ethereum first described in Vitalik Buterin's white paper.

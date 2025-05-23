#show-card

## Overview

Ethereum is a decentralized, open-source blockchain platform that enables the creation and deployment of [[Smart contract]]s and decentralized applications (dApps). Launched in 2015 by [[Vitalik buterin]] and a team of co-founders, Ethereum introduced the revolutionary concept of a programmable blockchain, often described as a "world computer." Its native cryptocurrency, Ether (ETH), serves multiple crucial functions within the ecosystem, including paying for transaction fees (gas), participating in the network's consensus mechanism through staking, and acting as a primary store of value and collateral in the [[Decentralized finance]] space. Ethereum is undergoing continuous development through a series of ambitious upgrades aimed at enhancing its scalability, security, and sustainability, with the long-term vision of becoming the global settlement layer for a wide array of Web3 applications.

- **Problem Solved:** Ethereum addresses the limitations of earlier blockchains like Bitcoin by providing a Turing-complete execution environment (the [[EVM]]), allowing for complex, arbitrary code to be run on the blockchain. This enables trustless, programmable transactions and the creation of sophisticated dApps, moving beyond simple peer-to-peer electronic cash systems.
- **Value Proposition:** As the most widely adopted smart contract platform, Ethereum boasts the largest and most active developer ecosystem, a vast network effect, and a proven track record of innovation and resilience. Its continuous evolution ensures it remains at the forefront of blockchain technology.
- **Official Website:** [Official Ethereum Website](https://ethereum.org)
- **Status:** Live, with a roadmap of significant ongoing and future upgrades (e.g., The Merge (completed), [[Dencun upgrade]] (completed), [[Pectra upgrade]] (upcoming)).

## Key Features

- **Smart Contracts:** Self-executing programs deployed on the blockchain that automate agreements and processes. They are the backbone of dApps, enabling complex logic for DeFi, NFTs, DAOs, and countless other applications.
- **Ethereum Virtual Machine ([[EVM]]):** The sandboxed runtime environment that executes Ethereum smart contracts. Its design ensures that code execution is deterministic and isolated, providing a universal standard for smart contract deployment and interaction across the network and EVM-compatible chains.
- **Account Abstraction (AA):** Aims to make user accounts (Externally Owned Accounts - EOAs) more flexible and programmable, similar to smart contracts. EIPs like those in the [[Pectra upgrade]] (e.g., EIP-7702) will allow EOAs to initiate operations like transaction batching and gas sponsorship, significantly improving user experience.
- **Staking & [[Proof of stake]] (PoS):** Following [[The Merge]], Ethereum transitioned to a PoS consensus mechanism. Users can stake their ETH to participate as [[Validator]]s, proposing and attesting to new blocks, securing the network, and earning ETH rewards. This is managed by the [[Beacon chain]].
- **Scalability Solutions:** Ethereum actively supports and fosters a multi-pronged approach to scalability, primarily through Layer 2 solutions like [[Rollup]]s ([[Optimism]], [[Arbitrum]], [[Linea]]) that process transactions off-chain and post data back to Ethereum. Upgrades like the [[Dencun upgrade]] (introducing blobspace) significantly reduce data posting costs for L2s.
- **Upgradeable Protocol & Roadmap:** Ethereum evolves through a community-driven process of Ethereum Improvement Proposals (EIPs) and network upgrades (hard forks). Key past upgrades include The Merge (PoS transition) and London ([[EIP-1559]]). Future upgrades like [[Pectra upgrade]] continue this evolution, focusing on areas like staking, account abstraction, and further scalability enhancements.

## Technology

- **Blockchain/Platform:** A standalone, decentralized public blockchain.
- **Architecture:** Employs a layered architecture:
  - **Execution Layer (EL):** Responsible for transaction processing, smart contract execution (via the [[EVM]]), and maintaining the Ethereum state. This is the layer users and dApps primarily interact with.
  - **Consensus Layer (CL) - [[Beacon chain]]:** Manages the [[Proof of stake]] consensus mechanism. It coordinates the network of [[Validator]]s, processes attestations, proposes blocks, and ensures agreement on the canonical chain. The EL receives its consensus from the CL.
- **Core Mechanisms:**
  - **Consensus:** [[Proof of stake]] (since [[The Merge]], September 2022), orchestrated by the [[Beacon chain]].
  - **Transaction Fee Model:** [[EIP-1559]] introduced a base fee (burned) that adjusts to network demand and an optional priority fee (tip) for validators.
  - **Data Availability for L2s:** Blob-carrying transactions (via [[Dencun upgrade]]) provide a cost-effective way for L2s to post data to Ethereum.
- **Smart Contracts:** Primarily written in Solidity, Vyper, and other EVM-compatible languages. Numerous open-source libraries and audited contract patterns are available (see [[Awesome ethereum]] for resources).

## Ecosystem & Use Cases

- **Target Audience:** Developers building dApps, DeFi users and protocols, NFT creators and collectors, DAOs, enterprises exploring blockchain solutions, and individuals seeking a decentralized financial and application platform.
- **How It's Used:**
  - **DeFi:** Lending, borrowing, decentralized exchanges (DEXs), yield farming, stablecoins.
  - **NFTs:** Minting, trading, and showcasing digital art, collectibles, and in-game items.
  - **DAOs:** Decentralized governance for protocols and communities.
  - **Gaming:** Play-to-earn models, on-chain game logic, and asset ownership.
  - **Identity & Social:** Decentralized identity solutions and Web3 social platforms.
- **Integrations:**
  - **Layer 2s:** [[Optimism]], [[Arbitrum]], [[Linea]], and many others.
  - **Wallets:** [[MetaMask]], Ledger, Trezor, and a wide array of software and hardware wallets.
  - **Infrastructure Providers:** [[Infura]], [[Alchemy]], and other node service providers.
  - **Developer Tools:** Truffle, Hardhat, Foundry, Remix IDE.
- **Tokenomics (ETH):**
  - **Utility:** ETH is essential for network operation:
    - **Gas Fees:** Paying for computation and storage on the network ([[EIP-1559]] model).
    - **Staking:** Required to become a [[Validator]] in the PoS consensus (32 ETH per validator).
    - **Collateral:** Widely used as collateral in DeFi protocols.
    - **Medium of Exchange:** Primary currency within the Ethereum ecosystem for NFTs, services, etc.
  - **Issuance:** New ETH is issued as rewards to validators for proposing and attesting to blocks on the [[Beacon chain]]. Post-Merge, issuance was significantly reduced compared to the previous PoW model.
  - **Supply Mechanism & EIP-1559:** The [[EIP-1559]] mechanism burns the base fee portion of transaction fees. This burning, combined with the reduced PoS issuance, can make ETH deflationary during periods of high network activity (i.e., when burned ETH exceeds new issuance).
  - **See also:** [[Awesome ethereum]] for more on tokens and DeFi protocols.

## Getting Started & Resources

- **Access:** Interact via wallets like [[MetaMask]], or run your own Ethereum node.
- **Documentation:** [Official Ethereum Docs](https://ethereum.org/en/developers/docs/)
- **Community:** [Ethereum Discord](https://discord.com/invite/CetY6Y4), [r/ethereum Reddit](https://reddit.com/r/ethereum), [@ethereum Twitter](https://twitter.com/ethereum)
- **Support:** [Ethereum Support Page](https://support.ethereum.org/)
- **Source Code:** [Ethereum on GitHub](https://github.com/ethereum)

## Team and Project History

Ethereum was co-founded by a group of individuals including [[Vitalik buterin]], Gavin Wood, Joseph Lubin, Charles Hoskinson, Anthony Di Iorio, Mihai Alisie, Jeffrey Wilcke, and Amir Chetrit. The Ethereum Foundation, a non-profit organization, plays a significant role in supporting the research, development, and education related to Ethereum and its ecosystem. The project's history is marked by a series of significant upgrades, detailed in the "Latest Updates" section below, reflecting its ongoing evolution and community-driven development process.

## Comparative Analysis

Ethereum is often compared to other blockchain platforms, each with different design goals and trade-offs:

- **Bitcoin:** While Bitcoin was the pioneering blockchain primarily designed as a peer-to-peer electronic cash system, Ethereum introduced a programmable layer with [[Smart contract]] capabilities. Bitcoin focuses on being a secure store of value, whereas Ethereum aims to be a decentralized "world computer" for a wide range of applications.
- **Newer Layer 1s (e.g., [[Solana]], [[Polkadot]], [[Avalanche]]):** Many newer Layer 1 blockchains were designed to address the scalability challenges initially faced by Ethereum. They often employ different consensus mechanisms, execution environments, or sharding techniques to achieve higher throughput and lower transaction fees. However, Ethereum maintains the largest network effect, developer community, and a robust ecosystem of Layer 2 scaling solutions like [[Rollup]]s to address these challenges.
  - **[[Solana]]:** Focuses on high throughput via its Proof of History (PoH) consensus mechanism and parallel transaction processing.
  - **[[Polkadot]]:** Emphasizes interoperability through its parachain architecture, allowing specialized blockchains to connect and communicate.
  - **[[Avalanche]]:** Uses a novel consensus protocol to achieve fast finality and supports subnetworks for custom blockchain creation.
- **EVM-Compatible Chains (e.g., [[BNB chain]], [[Polygon]]):** These chains leverage Ethereum's [[EVM]], allowing for easy porting of Ethereum dApps. They often offer lower fees and faster transactions but might have different decentralization or security trade-offs compared to Ethereum mainnet. Ethereum's strategy incorporates Layer 2 solutions as the primary scaling method while maintaining its security and decentralization.

Ethereum's approach to scaling via Layer 2 solutions and its continuous protocol upgrades (like [[Dencun upgrade]] and the upcoming [[Pectra upgrade]]) aim to maintain its leading position while addressing its historical limitations.

## Related Concepts

- [[Beacon chain]]
- [[Dencun upgrade]]
- [[EIP-1559]]
- [[EVM]]
- [[Pectra upgrade]]
- [[Proof of stake]]
- [[Rollup]]
- [[Smart contract]]
- [[Staking]]
- [[The Merge]]
- [[Validator]]
- [[Vitalik buterin]]
- [[Awesome ethereum]]

## Latest Updates

- **[[Pectra upgrade]] (Upcoming ~Q1 2025):** Next major upgrade focusing on staking improvements (EIP-7251, EIP-7002), Account Abstraction enhancements (EIP-7702), and further L2 scaling support.
- **[[Dencun upgrade]] (March 2024):** Introduced Proto-Danksharding with blob transactions, significantly reducing Layer 2 data posting costs.
- **[[The Merge]] (September 2022):** Ethereum successfully transitioned from Proof-of-Work to [[Proof of stake]] consensus, drastically reducing energy consumption by ~99.95% and changing ETH issuance dynamics.
- **London Hard Fork (August 2021):** Implemented [[EIP-1559]], overhauling the transaction fee market and introducing ETH burning.
- **Berlin Upgrade (April 2021):** Optimized gas costs for certain EVM operations.
- **Beacon Chain Genesis (December 2020):** The [[Proof of stake]] [[Beacon chain]] launched, running in parallel with the PoW mainnet until [[The Merge]].
- **Homestead (March 2016):** First production-ready version of Ethereum.
- **Frontier (July 2015):** Initial live release of Ethereum.
- **2013-2014:** Ethereum concept first described in [[Vitalik buterin]]'s white paper (2013), followed by crowdsale and development.

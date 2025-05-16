#show-card

## Overview

Astar Network is a scalable, interoperable, and multi-virtual machine smart contract platform built as a parachain on the [[Polkadot]] network. It aims to be a leading dApp (decentralized application) hub, connecting the Polkadot ecosystem to [[Ethereum]], Cosmos, and other major blockchains. Originally known as Plasm Network, it rebranded to Astar Network in September 2021.

Astar Network addresses the challenges of scalability and interoperability in the blockchain space. It provides a robust infrastructure for developers to build and deploy complex dApps by supporting both [[EVM]] and WASM (WebAssembly) environments. This dual compatibility allows developers to leverage existing Ethereum tools and codebases while also exploring the performance and flexibility benefits of WASM.

**Value Proposition:**

- **Multi-Chain Smart Contract Hub:** Astar serves as a gateway for smart contracts to and from the Polkadot ecosystem.
- **Scalability:** Leveraging Polkadot's shared security and parachain architecture, Astar aims for high transaction throughput and low fees.
- **Interoperability:** Designed to connect various Layer 1 blockchains.
- **Developer Incentives:** Through its unique `dApp Staking` mechanism, developers can earn rewards for building on the network.
- **Multi-VM Support:** Supports both EVM and WASM, offering flexibility to developers.

**Official Website:** [Astar Network](mdc:https://astar.network/)

**Status & Roadmap:**
Astar Network is live and actively developing its ecosystem. Key milestones include its successful parachain auction win on Polkadot. The "Astar Evolution" initiative marks its expansion strategy, including integration with Soneium (an [[Ethereum]] Layer 2 solution by Sony) and the OP Superchain ecosystem to enhance growth and interoperability.

## Key Services/Features

- **dApp Staking:** A unique incentive mechanism where users can stake ASTR tokens on dApps listed on the Astar Network. Both stakers and dApp developers earn rewards, encouraging ecosystem growth and dApp development.
- **Multi-Virtual Machine (Multi-VM):**
  - **EVM Compatibility:** Allows developers to deploy existing [[Ethereum]] smart contracts written in Solidity with minimal changes.
  - **WASM Support:** Enables the use of high-performance smart contracts written in languages like Rust (via ink!).
- **Cross-Chain Messaging (XCM):** Leverages Polkadot's XCM format to enable seamless communication and asset transfers with other parachains in the Polkadot ecosystem.
- **Layer 2 Solutions Integration:** Astar is expanding to incorporate Layer 2 scaling solutions. Its collaboration with Soneium aims to provide an Ethereum Layer 2 solution, enhancing scalability and offering low-cost transactions.
- **Astar Portal:** A user-friendly interface for interacting with the Astar ecosystem, including staking, dApp discovery, and asset management.

## Technology

- **Blockchain/Platform:** Built on the Substrate framework, Astar operates as a parachain on the [[Polkadot]] network, benefiting from Polkadot's shared security and interoperability features. It is also integrating with [[Ethereum]] Layer 2 solutions like Soneium, which is built on the OP Stack (related to [[Optimism]]).
- **Architecture:**
  - **Parachain on Polkadot:** Astar connects to the Polkadot Relay Chain, which handles consensus and security.
  - **Multi-VM Layer:** Provides parallel support for EVM and WASM execution environments.
  - **dApp Staking Layer:** Manages the staking and reward distribution for dApps and stakers.
- **Core Mechanism(s):**
  - **Build2Earn:** The overarching model that includes dApp Staking, allowing developers to earn a basic income by building and maintaining dApps on Astar.
  - **Substrate Framework:** Provides a modular and flexible foundation for building blockchains.
- **Smart Contracts:**
  - Supports Solidity for EVM.
  - Supports ink! (Rust-based eDSL) for WASM.
  - Developers can find information on deploying and interacting with smart contracts via Astar's official documentation. Audit reports for core components and supported dApps are typically made available by the respective teams.

## Ecosystem & Use Cases

- **Target Audience:**
  - **dApp Developers:** Seeking a scalable and interoperable platform with financial incentives.
  - **DeFi Users:** Accessing various decentralized finance applications.
  - **NFT Projects:** Utilizing the platform for NFT minting and marketplaces.
  - **Enterprises:** Exploring blockchain solutions with Astar's robust infrastructure.
- **How it's Used (Detailed Use Cases):**
  - **DeFi:** Building and using decentralized exchanges (DEXs), lending protocols, and stablecoins.
  - **NFTs:** Creating, trading, and managing non-fungible tokens and marketplaces.
  - **Gaming:** Developing and playing blockchain-based games.
  - **DAOs:** Establishing and managing decentralized autonomous organizations.
- **Integrations:** Astar integrates with various projects and tools within the Polkadot and Ethereum ecosystems. It actively fosters partnerships to expand its reach, including notable collaborations with entities like Sony for the Soneium L2.
- **Tokenomics (ASTR):**
  - **Utility:** The ASTR token is the native utility token of the Astar Network.
    - Transaction fees (gas).
    - Participation in dApp Staking.
    - On-chain governance.
    - Collator staking to support network operations.
  - **Supply Metrics:** Information on total supply, circulating supply, and max supply can be found on token tracking websites like CoinMarketCap or CoinGecko.
  - **Distribution & Emission:** Details are typically outlined in the project's official documentation.

## Getting Started & Resources

- **Accessing:**
  - **Astar Portal:** [portal.astar.network](mdc:https://portal.astar.network/)
  - **Wallets:** Compatible with Polkadot JS Extension, [[MetaMask]] (for EVM), and other Substrate-compatible wallets.
- **Comprehensive Documentation:** [Astar Docs](mdc:https://docs.astar.network/)
- **Community Channels:**
  - **Discord:** (Link usually found on the official website)
  - **Telegram:** (Link usually found on the official website)
  - **Forum:** (Link usually found on the official website)
- **Source Code:** [Astar Network GitHub](mdc:https://github.com/AstarNetwork) (Primarily licensed under Apache 2.0)

## Team and Project History

- **Team:** Led by Sota Watanabe (Founder & CEO). The team consists of experienced blockchain developers and researchers.
- **Project History & Milestones:**
  - Started as Plasm Network.
  - Won a Polkadot parachain slot in 2021.
  - Launched mainnet on Polkadot.
  - Continuous development and ecosystem growth through initiatives like Astar Evolution, focused on multi-chain expansion with Soneium and the Superchain.

## Comparative Analysis

- **Similar Projects:**
  - **Other Polkadot Parachains with Smart Contract Capabilities:** e.g., [[Moonbeam]], [[Acala]]. Astar differentiates with its strong focus on WASM, dApp Staking, and multi-chain vision.
  - **Layer 1 Smart Contract Platforms:** e.g., [[Ethereum]], [[Solana]], [[Avalanche]]. Astar aims to offer better scalability and interoperability through its Polkadot foundation and multi-VM approach.
  - **Layer 2 Scaling Solutions:** While Astar is a Layer 1 parachain, its integration with solutions like Soneium (an L2 for Ethereum) positions it within the broader scaling narrative.
- **Comparison Points:**
  - **Technology Stack:** Astar's Substrate base and dual VM (EVM/WASM) support.
  - **Ecosystem Focus:** Emphasis on dApp Staking as an incentive model.
  - **Interoperability:** Native interoperability within Polkadot and bridges to other ecosystems.
  - **Community & Traction:** Growing developer and user community.

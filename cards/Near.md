#show-card

# NEAR Protocol

## Overview

NEAR Protocol is a layer-1 blockchain designed to be user-friendly, scalable, and developer-oriented. Launched in April 2020, NEAR aims to address the limitations of earlier blockchain platforms by providing infrastructure for the open web and decentralized applications. Its key innovation is the implementation of sharding technology called Nightshade, which enhances scalability without compromising security or decentralization.

NEAR solves blockchain scalability issues through its unique sharding approach, allowing the network to process transactions in parallel across multiple shards, thereby increasing throughput capacity significantly compared to non-sharded blockchains.

The platform offers human-readable account names instead of cryptographic addresses, low transaction fees, and carbon-neutral operations, making it accessible to mainstream users.

**Official Website**: [NEAR Protocol](https://near.org)

**Status & Roadmap**: Live mainnet with continuous development. The project has completed several major milestones, including implementing Phase 0 of Nightshade sharding and launching the Aurora EVM environment. Future development focuses on expanding cross-chain capabilities, improving developer tooling, and advancing sharding implementation.

## Key Services/Features

### User-Friendly Accounts

NEAR uses human-readable account names (e.g., "username.near") rather than cryptographic addresses, significantly improving user experience. Accounts can be created easily through email or social media authentication, removing a major barrier to blockchain adoption.

### Rainbow Bridge

A trustless bridge connecting NEAR to [[Ethereum]] and other blockchains, enabling seamless asset transfer between ecosystems. Users can move tokens and data across chains without centralized intermediaries, expanding interoperability in the Web3 space.

### Developer-Friendly Environment

NEAR provides comprehensive SDKs supporting multiple programming languages (JavaScript/TypeScript, Rust, AssemblyScript), extensive documentation, and development tools that significantly reduce the learning curve for building decentralized applications.

### Aurora EVM

Aurora is an Ethereum Virtual Machine ([[EVM]]) implementation running as a contract on NEAR. It allows developers to deploy Ethereum smart contracts to NEAR with minimal modifications, taking advantage of NEAR's lower fees and higher throughput while maintaining compatibility with Ethereum tools and workflows.

## Technology

### Blockchain/Platform

NEAR Protocol is a standalone, independent layer-1 blockchain with its own consensus mechanism and native token.

### Architecture

NEAR utilizes a sharded architecture called Nightshade that splits the network into multiple shards, each processing transactions in parallel. This design enables horizontal scaling, allowing transaction throughput to increase proportionally with network growth.

The platform employs a "chunk-based" approach where the blockchain is divided into chunks assigned to different validators, rather than requiring all validators to process all transactions. This enables efficient use of network resources and supports high scalability.

### Core Mechanism(s)

#### Nightshade Sharding

Unlike traditional sharding where each shard maintains a separate blockchain, Nightshade creates a single blockchain where each block contains only a subset of all transactions (chunks). Validators are assigned to specific shards but collectively produce blocks for the entire chain, maintaining both high performance and strong security guarantees.

#### Doomslug Consensus

NEAR uses a Proof-of-Stake consensus algorithm called Doomslug that enables fast finality (typically 1-2 seconds) with minimal overhead. Validators are selected proportionally to their stake, and block production rights rotate among [[Validator|validators]] to ensure fair participation.

#### Contract-based Account Model

NEAR's account system is built on smart contracts, giving each account programmable capabilities. This design enables advanced features like account recovery, delegated actions, and complex permission structures without requiring protocol-level changes.

### Smart Contracts

NEAR supports [[Smart contract|smart contracts]] written in Rust, AssemblyScript, and through Aurora, [[Solidity]]. Contracts are compiled to WebAssembly (Wasm), providing efficient execution and language flexibility. The platform features a unique state staking model where developers pay for storage based on the amount of data their contracts store. While the core NEAR platform undergoes rigorous testing and security reviews, specific dApps and [[Smart contract|smart contracts]] built on NEAR should also undergo independent security audits. Users are encouraged to verify the audit status of individual applications.

Key contracts include:

- Account contracts (every account is a contract)
- Fungible Token (NEP-141) and Non-Fungible Token (NEP-171) standards
- Staking and validation contracts

## Ecosystem & Use Cases

### Target Audience

- **Developers**: Web and blockchain developers seeking a user-friendly platform with low barriers to entry
- **DeFi Users**: Traders and investors looking for high throughput and low fees, engaging with [[Decentralized finance]] applications.
- **NFT Creators and Collectors**: Artists and enthusiasts utilizing NEAR's efficient NFT infrastructure
- **DAO Participants**: Community members leveraging NEAR's governance tools and participating in Decentralized Autonomous Organizations (DAOs).
- **End Users**: Mainstream users accessing decentralized applications through NEAR's simplified user experience

### How it's Used

#### DeFi Applications

Users can engage with decentralized exchanges like Ref Finance to swap tokens with minimal fees. For example, a user can connect their NEAR wallet, deposit assets, and trade with significant cost savings compared to Ethereum-based alternatives, while enjoying almost instant transaction finality.

#### NFT Marketplaces

Creators can mint NFTs on platforms like Paras or Mintbase with low costs and list them for sale. Collectors can discover and purchase digital art, with transactions settling in seconds rather than minutes.

#### Cross-Chain Activities

Users can leverage Rainbow Bridge to move assets between NEAR and other blockchains. For instance, a user can transfer ETH from Ethereum to NEAR, use it within NEAR's ecosystem at lower costs, and then transfer it back when needed.

### Integrations

- **Aurora**: [[EVM]] environment enabling Ethereum compatibility
- **Octopus Network**: Interoperable appchain network built on NEAR
- **Flux Protocol**: [[Oracle]] solution providing off-chain data
- **[[Chainlink]]**: [[Oracle]] integration for reliable external data
- **Ceramic Network**: Decentralized data network integration

### Tokenomics

NEAR token serves multiple purposes within the ecosystem:

- Payment for transaction fees
- Staking for network security
- Governance participation

**Total Supply**: 1 billion NEAR tokens
**Distribution**: 17.2% to community grants, 23.7% to ecosystem development, 11.4% to early backers, 10% to foundation endowment, and the remaining to the team and other stakeholders
**Emission**: Dynamic supply with an initial inflation rate of 5%, which decreases over time as transaction fee burning mechanism balances new issuance

## Getting Started & Resources

### Accessing

- Create a NEAR account at [NEAR Wallet](https://wallet.near.org)
- Access the NEAR blockchain explorer at [NEAR Explorer](https://explorer.near.org)
- Develop applications using [NEAR SDK](https://docs.near.org/sdk/welcome)

### Comprehensive Documentation

- [NEAR Protocol Documentation](https://docs.near.org)
- [NEAR Developer Documentation](https://docs.near.org/develop/welcome)

### Community Channels

- [NEAR Discord](https://near.chat)
- [NEAR Forum](https://gov.near.org)
- [NEAR Twitter](https://twitter.com/nearprotocol)

### Support Resources

- [NEAR Help Center](https://help.near.org)
- [NEAR Stack Exchange](https://near.stackexchange.com)

### Source Code

- [NEAR GitHub](https://github.com/near)
- Open source under Apache 2.0 and MIT licenses

## Team and Project History

### Team

NEAR was founded by Alex Skidanov (former Director of Engineering at MemSQL) and Illia Polosukhin (former Engineering Lead at Google). The core team includes veterans from major tech companies and blockchain projects, with expertise spanning distributed systems, cryptography, and user experience design.

### Project History & Milestones

- **2018**: NEAR Protocol conceptualized
- **2019**: Raised $12.1M in venture funding
- **April 2020**: Mainnet launched with Proof-of-Authority consensus
- **October 2020**: Transitioned to community-governed Proof-of-Stake
- **2021**: Launched Rainbow Bridge and Aurora EVM
- **2022**: Implemented Phase 0 of Nightshade sharding and surpassed 100M accounts
- **2023**: Expanded ecosystem with over 1000 projects building on NEAR

## Comparative Analysis

### NEAR Protocol vs. Ethereum

Both are smart contract platforms, but NEAR offers significantly lower transaction fees and higher throughput. While Ethereum has broader adoption and a larger ecosystem, NEAR provides a more user-friendly experience with human-readable accounts. NEAR's sharded architecture allows for better scalability today, though Ethereum's transition to ETH2 aims to address these limitations.

### NEAR Protocol vs. Solana

Both focus on high throughput and low fees, but through different approaches. [[Solana]] achieves performance through a single high-performance chain with specialized hardware requirements, while NEAR uses sharding to distribute the load. NEAR offers better developer experience with more accessible programming models, while [[Solana]] provides higher raw performance but with more centralized [[Validator|validator]] requirements.

### NEAR Protocol vs. Cosmos

Both support interoperability, but with different philosophies. Cosmos creates an "internet of blockchains" where each app can have its own chain, while NEAR uses sharding within a single blockchain. NEAR provides a more unified experience and shared security model, whereas Cosmos offers greater sovereignty for individual applications at the cost of more complex interchain security arrangements.

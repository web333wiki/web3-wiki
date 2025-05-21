#show-card

## Overview

Polygon is a multi-faceted platform for [[Ethereum]] scaling and infrastructure development. Initially known for its Proof-of-Stake (PoS) sidechain, Polygon has evolved into a comprehensive suite of solutions aimed at transforming Ethereum into a multi-chain ecosystem, or an "Internet of Blockchains." It offers developers a variety of tools and technologies to build scalable decentralized applications (dApps), including its PoS chain, Polygon SDK for building standalone chains, and a growing focus on [[Layer 2]] solutions like ZK-rollups.

The core mission of Polygon is to provide scalable, affordable, secure, and easy-to-use infrastructure for Web3 applications. It addresses Ethereum's limitations of high gas fees and network congestion by offering faster and cheaper transactions, while still benefiting from Ethereum's security and network effects.

Unique benefits of Polygon include its diverse range of scaling solutions catering to different needs, from the battle-tested PoS chain to cutting-edge ZK-rollup technologies. Its MATIC token plays a crucial role in securing the network (via staking on the PoS chain) and for paying transaction fees. Key differentiators are its commitment to becoming a ZK-powerhouse with multiple ZK-rollup solutions under development (Polygon zkEVM, Miden, Zero, Nightfall) and its vision for a fully interoperable multi-chain future with Polygon 2.0.

Polygon was co-founded by Jaynti Kanani, Sandeep Nailwal, Anurag Arjun, and Mihailo Bjelic. It was formerly known as Matic Network. Key milestones include the launch of the Matic PoS mainnet, rebranding to Polygon, significant ecosystem growth, strategic acquisitions in the ZK space (e.g., Hermez Network, Mir Protocol), the launch of Polygon zkEVM mainnet beta, and the ongoing proposal and development of Polygon 2.0, which aims to unify its various solutions into a cohesive ZK-powered L2 ecosystem.

### Get Started with Polygon

| Resource         | Link                                                                                                                             | Description                                                    |
| ---------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------- |
| Official Website | [https://polygon.technology/](https://polygon.technology/)                                                                       | Main website for Polygon, its solutions, and ecosystem.        |
| Developer Docs   | [https://docs.polygon.technology/](https://docs.polygon.technology/)                                                             | Comprehensive documentation for developers.                    |
| Polygon PoS      | [https://polygon.technology/polygon-pos/](https://polygon.technology/polygon-pos/)                                               | Information about the Polygon Proof-of-Stake chain.            |
| Polygon zkEVM    | [https://polygon.technology/polygon-zkevm/](https://polygon.technology/polygon-zkevm/)                                           | Information about Polygon's ZK-Rollup EVM-equivalent solution. |
| Bridge           | [https://wallet.polygon.technology/polygon/bridge](https://wallet.polygon.technology/polygon/bridge)                             | Official bridge for transferring assets to/from Polygon PoS.   |
| PoS Explorer     | [https://polygonscan.com/](https://polygonscan.com/)                                                                             | Block explorer for the Polygon PoS chain.                      |
| zkEVM Explorer   | [https://zkevm.polygonscan.com/](https://zkevm.polygonscan.com/)                                                                 | Block explorer for the Polygon zkEVM.                          |
| GitHub           | [https://github.com/maticnetwork](https://github.com/maticnetwork), [https://github.com/0xPolygon](https://github.com/0xPolygon) | Source code and repositories.                                  |
| Community        | Links on the main website                                                                                                        | Access to Discord, Telegram, and other community channels.     |
| Twitter          | [https://twitter.com/0xPolygon](https://twitter.com/0xPolygon)                                                                   | Official Twitter account for news and updates.                 |

## Key Services/Features

### Polygon PoS Chain

The Polygon PoS chain is a Proof-of-Stake sidechain that runs in parallel to [[Ethereum]], offering fast and low-cost transactions. It achieves scalability by having its own set of validators and consensus mechanism while periodically committing checkpoints to the Ethereum mainnet for security.
Its underlying technology uses a dual strategy of Proof of Stake (PoS) at the checkpointing layer and Block Producers at the block producer layer to achieve faster block times. While it is often referred to as a [[Layer 2]], it's more accurately described as a sidechain that bridges to Ethereum, offering a different security model than pure L2s that directly inherit Ethereum's security for every transaction.
Real-world use cases are extensive, covering [[Decentralized finance]] (DeFi), NFTs, gaming, enterprise applications, and more. Many major Ethereum dApps have deployed versions on Polygon PoS to reach a wider audience. Documentation is available at [Polygon PoS Docs](https://docs.polygon.technology/docs/pos/polygon-architecture).

### Polygon zkEVM (Mainnet Beta)

Polygon zkEVM is a [[Layer 2]] scaling solution that uses Zero-Knowledge (ZK) rollup technology to bundle transactions and validate them on [[Ethereum]] using ZK proofs. It is designed to be EVM-equivalent, meaning most Ethereum smart contracts and developer tools work seamlessly on Polygon zkEVM.
The technology leverages zk-SNARKs (Zero-Knowledge Succinct Non-Interactive Argument of Knowledge) to prove the validity of off-chain transaction batches to the Ethereum mainnet. This provides strong security guarantees inherited from Ethereum, combined with high throughput and low fees. It aims for "Type 2" EVM equivalence, striving for compatibility at the bytecode level.
Use cases include dApps requiring high security and scalability, such as DeFi protocols and NFT marketplaces that want to leverage the benefits of ZK technology without rewriting their existing Solidity code. More details can be found at [Polygon zkEVM Docs](https://docs.polygon.technology/docs/zkevm/).

### Polygon Miden (Alpha Testnet)

Polygon Miden is a STARK-based ZK-Rollup currently under development. It aims to extend [[Ethereum]]'s feature set by supporting arbitrary logic and parallel transaction execution through its Miden VM, which is designed for ZK-friendliness.
The Miden VM uses STARK proofs, which are known for their transparency (no trusted setup) and scalability. A key feature is client-side proving, where users can generate proofs of their transactions locally, enhancing privacy and efficiency. It is not directly EVM-compatible but will allow for Solidity contracts to be compiled to its VM.
Potential use cases include private transactions, complex computations, and applications that can benefit from concurrent transaction processing and local proving.

### Polygon Zero (Acquired Mir Protocol)

Polygon Zero (formerly Mir Protocol) specializes in developing highly efficient ZK-rollup technology, particularly focusing on recursive ZK proofs (Plonky2). Plonky2 is a proving system that combines the benefits of PLONK (fast proofs, universal trusted setup) and FRI (no trusted setup, STARK-like recursion) to achieve fast and scalable proof generation.
The technology allows for extremely fast proof generation, even on consumer hardware, which is crucial for building performant ZK-rollups. This efficiency is key to scaling [[Ethereum]] transactions to a massive degree.
Its primary application is to power fast and efficient ZK-rollups within the Polygon ecosystem, contributing to the overall scalability vision.

### Polygon Nightfall

Polygon Nightfall is a privacy-focused rollup solution developed in collaboration with EY. It combines Optimistic Rollups with ZK-cryptography to enable private transactions for enterprises.
It aims to provide businesses with a way to conduct transactions on a public blockchain like [[Ethereum]] while keeping sensitive data confidential. It uses ZK proofs for privacy and optimistic rollups for scalability.
Use cases are primarily enterprise-focused, such as private supply chain management, tokenized assets with privacy, and other business processes requiring confidentiality on a shared ledger.

### Polygon SDK

The Polygon SDK is a modular and extensible framework for building [[Ethereum]]-compatible blockchain networks. It allows developers to launch standalone chains or secure chains (L2s) that connect to Ethereum.
It provides various modules (e.g., consensus, networking, EVM) that can be customized to create application-specific blockchains with their own governance and tokenomics, similar in concept to Cosmos SDK or Polkadot's Substrate.
This enables projects to create sovereign chains tailored to their specific needs while still being able to connect to the broader Ethereum and Polygon ecosystems.

### Polygon 2.0

Polygon 2.0 is a proposed upgrade and vision for the future of Polygon. It aims to unify Polygon's various scaling solutions (PoS, zkEVM, Supernets) into a cohesive network of ZK-powered [[Layer 2]] chains that are interconnected and share security, ultimately forming a "value layer" for the internet.
The architecture proposes a Staking Hub to manage validators across different Polygon chains, an Interop Layer for cross-chain communication, and unified tokenomics with the POL token (upgraded from MATIC). It envisions a future where developers can easily deploy ZK L2s.
This is a long-term vision to create a highly scalable and interoperable ecosystem built on ZK technology.

## Comparative Analysis

Polygon's multi-solution approach makes direct comparisons complex. Its PoS chain competes with other sidechains and fast L1s, while its ZK-rollups compete with solutions like [[Arbitrum]], [[Optimism]], and [[ZKSync]].

| Feature            | Polygon PoS                                     | Polygon zkEVM                                 | Arbitrum One                                   | Optimism Bedrock                            | zkSync Era                                          |
| ------------------ | ----------------------------------------------- | --------------------------------------------- | ---------------------------------------------- | ------------------------------------------- | --------------------------------------------------- |
| Technology         | PoS Sidechain                                   | ZK-Rollup (zk-SNARKs)                         | Optimistic Rollup                              | Optimistic Rollup                           | ZK-Rollup (zk-SNARKs)                               |
| EVM Compatibility  | High (EVM-compatible)                           | High (EVM-equivalent, Type 2 goal)            | High (EVM-equivalent)                          | High (EVM-equivalent)                       | EVM-compatible (Solidity/Vyper via LLVM)            |
| Security Model     | Separate validator set, checkpoints to Ethereum | Inherits Ethereum security via ZK proofs      | Inherits Ethereum security, 7-day challenge    | Inherits Ethereum security, 7-day challenge | Inherits Ethereum security via ZK proofs            |
| Data Availability  | Own chain                                       | On-chain (Ethereum)                           | On-chain (Ethereum)                            | On-chain (Ethereum)                         | On-chain (Ethereum) or off-chain (zkPorter)         |
| Maturity           | Very mature, large ecosystem                    | Mainnet Beta, growing                         | Well-established, large ecosystem              | Well-established, growing ecosystem         | Mainnet Alpha, growing                              |
| Native Token       | MATIC (Gas, Staking)                            | ETH (for gas), MATIC (for sequencing/staking) | ETH (for gas), ARB (Governance)                | ETH (for gas), OP (Governance)              | ETH (for gas), future token expected                |
| Key Differentiator | Low fees, fast, large existing user base        | EVM-equivalent ZK-Rollup, part of Polygon 2.0 | Nitro upgrade performance, Stylus, mature tech | OP Stack, Superchain vision, RetroPGF       | Native Account Abstraction, zkPorter, LLVM compiler |

Polygon PoS offers a mature, high-speed, low-cost environment but with different security assumptions than L2 rollups. Polygon zkEVM aims to combine strong ZK security with EVM equivalence, placing it in direct comparison with other zkEVMs and optimistic rollups. The broader Polygon 2.0 vision with multiple ZK solutions (Miden, Zero) and an interop layer positions Polygon as a major research and development hub for ZK technology.

#show-card

## Overview

Arbitrum is a [[Layer 2]] scaling solution for [[Ethereum]], designed to address the network's challenges of high transaction fees and slow transaction speeds. It aims to make Ethereum applications faster, cheaper, and more scalable without sacrificing the security guarantees of the underlying Ethereum mainnet. Arbitrum achieves this primarily through Optimistic Rollup technology, processing transactions off-chain and then batching them together before submitting them to Ethereum.

The core mission of Arbitrum is to scale Ethereum and provide a significantly improved user experience for decentralized applications (dApps). It solves the problem of network congestion on Ethereum, which can lead to exorbitant gas fees and slow confirmation times, hindering adoption and usability.

Unique benefits and advantages of Arbitrum include its strong EVM-compatibility (making it easy for [[Ethereum]] developers to migrate their dApps), its robust security model that inherits security from Ethereum, and its vibrant and rapidly growing ecosystem. A key differentiator is its advanced fraud-proof system and the development of features like Arbitrum Stylus, which allows for smart contracts to be written in multiple programming languages beyond Solidity.

Arbitrum was developed by Offchain Labs, a company co-founded by Ed Felten, Steven Goldfeder, and Harry Kalodner, all with strong backgrounds in computer science and cryptography. Key milestones include the launch of Arbitrum One, the mainnet rollup chain, the significant performance upgrade with Arbitrum Nitro, the introduction of Arbitrum Nova (an AnyTrust chain optimized for gaming and social applications), and the launch of the ARB governance token.

### Get Started with Arbitrum

| Resource            | Link                                                               | Description                                                       |
| ------------------- | ------------------------------------------------------------------ | ----------------------------------------------------------------- |
| Official Website    | [https://arbitrum.io/](https://arbitrum.io/)                       | Main website for Arbitrum information.                            |
| Foundation          | [https://arbitrum.foundation/](https://arbitrum.foundation/)       | The foundation supporting the Arbitrum ecosystem and DAO.         |
| Developer Docs      | [https://developer.arbitrum.io/](https://developer.arbitrum.io/)   | Comprehensive documentation for developers building on Arbitrum.  |
| Bridge              | [https://bridge.arbitrum.io/](https://bridge.arbitrum.io/)         | Official bridge to transfer assets between Ethereum and Arbitrum. |
| Block Explorer      | [https://arbiscan.io/](https://arbiscan.io/)                       | Arbitrum One block explorer.                                      |
| Nova Explorer       | [https://nova.arbiscan.io/](https://nova.arbiscan.io/)             | Arbitrum Nova block explorer.                                     |
| GitHub              | [https://github.com/OffchainLabs](https://github.com/OffchainLabs) | Source code and repositories for Arbitrum.                        |
| Community (Discord) | Access via [Arbitrum Foundation](https://arbitrum.foundation/)     | Official Discord server for community discussions and support.    |
| Twitter             | [https://twitter.com/arbitrum](https://twitter.com/arbitrum)       | Official Twitter account for news and updates.                    |

## Key Services/Features

### Arbitrum One

Arbitrum One is the flagship [[Layer 2]] Optimistic Rollup chain for [[Ethereum]]. It is designed for general-purpose dApp deployment and aims to provide a highly scalable and low-cost environment for EVM-compatible smart contracts.
The underlying technology involves bundling transactions off-chain and submitting compressed data to the Ethereum mainnet. It uses an "optimistic" approach where transactions are assumed valid by default, but there's a challenge period during which anyone can submit a fraud proof if they detect an invalid state transition. The Nitro upgrade significantly improved its performance by compiling core Geth engine code to WASM.
Real-world use cases include a wide array of [[Decentralized finance]] (DeFi) protocols, NFT marketplaces, DAOs, and other dApps seeking to escape Ethereum's high gas fees. It allows for faster and cheaper swaps, lending, borrowing, and NFT minting/trading. Official documentation can be found at [developer.arbitrum.io/public-chains](https://developer.arbitrum.io/public-chains).

### Arbitrum Nova

Arbitrum Nova is another chain in the Arbitrum ecosystem, but it utilizes AnyTrust technology instead of being a pure Optimistic Rollup. AnyTrust chains are designed for ultra-low transaction fees and high throughput, making them suitable for applications like gaming, social media, and high-volume dApps where minor trust assumptions are acceptable for greater performance.
Nova relies on a Data Availability Committee (DAC) to store transaction data. This reduces costs compared to storing all data on [[Ethereum]] like Arbitrum One. However, it introduces an additional trust assumption on the honesty and availability of the DAC members. If the DAC fails, the chain can fall back to rollup mode, posting data to Ethereum.
Use cases for Nova focus on applications that require very frequent, low-value transactions, such as in-game actions, social tipping, or frequent micro-transactions. Official documentation can be found at [developer.arbitrum.io/public-chains](https://developer.arbitrum.io/public-chains).

### Arbitrum Orbit

Arbitrum Orbit allows projects to launch their own customizable Layer 3 (L3) chains that settle to an Arbitrum [[Layer 2]] chain (like Arbitrum One or Nova) or directly to Ethereum as a Layer 2. This enables developers to create application-specific chains with tailored features, throughput, and governance.
The technology allows for permissionless deployment of dedicated rollups or AnyTrust chains. Developers can configure aspects like gas token, privacy, and permissions. These L3s inherit security from their settlement layer (L2 or L1) while offering further scalability and customization.
Orbit chains can be used by projects wanting dedicated blockspace, predictable fees, and greater control over their environment, without building an L1 from scratch. Examples include game-specific chains or enterprise solutions. More information can be found on the [Arbitrum Orbit page](https://arbitrum.io/orbit).

### Arbitrum Stylus

Arbitrum Stylus is a significant upgrade that introduces a multi-language programming environment for smart contracts on Arbitrum chains. It allows developers to write smart contracts in languages like Rust, C, and C++, in addition to Solidity and other EVM languages, by compiling them to WebAssembly (WASM).
This feature greatly expands the developer pool for Arbitrum and allows for more performant and gas-efficient smart contracts due to the capabilities of languages like Rust and C++. Stylus contracts are interoperable with EVM contracts, meaning they can call each other seamlessly.
This opens up possibilities for more complex and computationally intensive applications on Arbitrum, leveraging the strengths of different programming languages. Details are available in the [Stylus documentation](https://developer.arbitrum.io/stylus/stylus-gentle-introduction).

## Comparative Analysis

Arbitrum is one of several leading [[Layer 2]] solutions for Ethereum. Its main competitors include [[Optimism]], [[Polygon]] (specifically its ZK-EVM and other L2 efforts), and [[ZKSync]].

| Feature            | Arbitrum (One)                                                   | Optimism (Bedrock)                                  | Polygon (ZK-EVM)                               | zkSync (Era)                                           |
| ------------------ | ---------------------------------------------------------------- | --------------------------------------------------- | ---------------------------------------------- | ------------------------------------------------------ |
| Technology         | Optimistic Rollup                                                | Optimistic Rollup                                   | ZK-Rollup (zk-SNARKs)                          | ZK-Rollup (zk-SNARKs)                                  |
| EVM Compatibility  | High (EVM-equivalent with Nitro)                                 | High (EVM-equivalent)                               | High (EVM-equivalent)                          | EVM-compatible (Solidity, Vyper via LLVM compiler)     |
| Fraud Proofs       | Interactive, multi-round proofs                                  | Single-round proofs                                 | Validity proofs (cryptographic)                | Validity proofs (cryptographic)                        |
| Data Availability  | On-chain (Ethereum)                                              | On-chain (Ethereum)                                 | On-chain (Ethereum) or off-chain options       | On-chain (Ethereum) or off-chain (zkPorter)            |
| Maturity           | Well-established, large ecosystem                                | Well-established, growing ecosystem                 | Newer, rapidly developing                      | Developing, focus on ZK innovations                    |
| Native Token       | ARB (Governance)                                                 | OP (Governance)                                     | MATIC (Gas, Staking, Governance on PoS chain)  | ETH (for gas), future token for decentralization       |
| Key Differentiator | Nitro upgrade performance, Stylus multi-language VM, mature tech | Simplicity of fraud proofs, OP Stack for Superchain | ZK-proofs for higher security, EVM equivalence | Native account abstraction, zkPorter data availability |

Arbitrum's Optimistic Rollup technology, particularly after the Nitro upgrade, offers a strong balance of EVM compatibility, speed, and cost-effectiveness. Its fraud-proofing system is more complex than Optimism's but aims to be more efficient. Compared to ZK-Rollups like Polygon ZK-EVM and zkSync, Optimistic Rollups generally have lower computational overhead for transaction processing but rely on a challenge period for finality, whereas ZK-Rollups provide faster finality once proofs are submitted. The introduction of Stylus also sets Arbitrum apart by broadening language support for smart contract development.

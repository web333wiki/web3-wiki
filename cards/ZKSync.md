#show-card

## Overview

zkSync is a [[Layer 2]] scaling protocol for [[Ethereum]] developed by Matter Labs. It leverages ZK-rollup technology to provide low-cost, scalable transactions without compromising on Ethereum's security. zkSync is designed to be EVM-compatible through its zkEVM, allowing developers to deploy existing Solidity and Vyper smart contracts with minimal friction. A key focus for zkSync is to provide a user experience that is as good as, or better than, traditional Web2 applications.

The core mission of zkSync is to accelerate the mass adoption of public blockchains by solving Ethereum's scalability problem through the power of zero-knowledge proofs. It aims to make crypto payments and dApp interactions significantly cheaper and faster, eventually capable of handling transaction volumes comparable to major centralized payment networks.

Unique benefits and advantages of zkSync include its strong emphasis on security through cryptographic validity proofs (ZK-SNARKs), native Account Abstraction (AA) for enhanced user experience (e.g., paying fees in any token, social recovery), and its LLVM-based compiler that supports a wider range of programming languages for smart contract development beyond just Solidity. Its zkPorter feature (currently under research for zkSync Era) aims to offer an off-chain data availability option for ultra-low fees.

zkSync is developed by Matter Labs, founded by Alex Gluchowski and Alex Vlasov. Key milestones include the launch of zkSync 1.0 (Lite) for payments and token transfers, the launch of zkSync 2.0 (now zkSync Era) mainnet alpha which introduced EVM compatibility and smart contract support, and ongoing research into zkPorter and further ZK-rollup optimizations.

### Get Started with zkSync

| Resource            | Link                                                               | Description                                                         |
| ------------------- | ------------------------------------------------------------------ | ------------------------------------------------------------------- |
| Official Website    | [https://zksync.io/](https://zksync.io/)                           | Main website for zkSync information and ecosystem.                  |
| Matter Labs         | [https://matter-labs.io/](https://matter-labs.io/)                 | Website of the company developing zkSync.                           |
| Developer Docs      | [https://era.zksync.io/docs/](https://era.zksync.io/docs/)         | Comprehensive documentation for developers building on zkSync Era.  |
| Bridge              | [https://portal.zksync.io/bridge](https://portal.zksync.io/bridge) | Official bridge to transfer assets between Ethereum and zkSync Era. |
| Block Explorer      | [https://explorer.zksync.io/](https://explorer.zksync.io/)         | zkSync Era block explorer.                                          |
| GitHub              | [https://github.com/matter-labs](https://github.com/matter-labs)   | Source code and repositories for zkSync.                            |
| Community (Discord) | [https://join.zksync.dev/](https://join.zksync.dev/)               | Official Discord server for community discussions and support.      |
| Twitter             | [https://twitter.com/zksync](https://twitter.com/zksync)           | Official Twitter account for news and updates.                      |

## Key Services/Features

### zkSync Era (Mainnet Alpha)

zkSync Era is the current mainnet version of zkSync, providing a general-purpose ZK-rollup platform that is EVM-compatible. It allows developers to deploy and interact with smart contracts written in Solidity, Vyper, and other languages supported by its LLVM-based compiler.
The underlying technology uses ZK-SNARKs to validate batches of transactions. These cryptographic proofs are then submitted to the [[Ethereum]] mainnet, ensuring that zkSync Era inherits Ethereum's security. Unlike Optimistic Rollups, ZK-rollups provide faster finality as transactions are proven valid cryptographically rather than relying on a challenge period. zkSync Era's zkEVM aims to achieve a high degree of compatibility with the EVM, allowing for easy migration of existing dApps.
Real-world use cases include [[Decentralized finance]] (DeFi) applications, NFT marketplaces, gaming, and any dApp that requires low transaction fees, high throughput, and strong security. The native Account Abstraction feature also opens up new possibilities for user-friendly dApp design. Official documentation can be found at [zkSync Era Documentation](https://era.zksync.io/docs/).

### Native Account Abstraction

zkSync Era was designed with native Account Abstraction (AA) from the ground up. This is a significant feature that enhances user experience and flexibility by allowing smart contract wallets to be first-class citizens.
With native AA, users can:

- Pay transaction fees in any token, not just ETH.
- Implement custom signature schemes (e.g., social recovery, multi-sig).
- Batch multiple transactions into one.
- Enable features like session keys or spending limits.
  This is different from [[Ethereum]] L1's EOA (Externally Owned Account) model and proposals like EIP-4337, as AA is integrated at the protocol level in zkSync Era, making it more powerful and seamless. This allows for wallet and dApp interactions that feel much closer to Web2 applications.

### LLVM-based Compiler

zkSync Era utilizes an LLVM (Low Level Virtual Machine) based compiler infrastructure. This is a significant technological choice that allows zkSync to support smart contracts written in a wider variety of programming languages beyond Solidity.
While Solidity and Vyper are the primary languages currently supported for its EVM-compatible zkEVM, the LLVM toolchain opens the door for future support of languages like Rust, C++, and Swift to be compiled into zkEVM bytecode. This can attract a broader developer base and enable more performant or specialized smart contracts.
This approach contrasts with other zkEVMs that might focus solely on direct transpilation or interpretation of EVM bytecode.

### zkPorter (Future Development)

zkPorter is a proposed off-chain data availability solution for zkSync. While ZK-rollups typically post all transaction data to [[Ethereum]] (on-chain data availability) for maximum security, zkPorter aims to offer an alternative where users can opt for data to be stored off-chain with a Data Availability Committee (DAC).
The benefit of zkPorter would be significantly lower transaction fees (potentially orders of magnitude cheaper) for users who are comfortable with the slightly different security assumptions of off-chain data availability. The system is designed such that accounts choosing on-chain data availability (rollup accounts) and zkPorter accounts can seamlessly interact. The security of zkPorter would rely on the honesty of a majority of the DAC members.
This feature is aimed at use cases requiring extremely high transaction volumes and very low costs, such as micropayments or certain types of gaming applications. Its development and implementation are part of Matter Labs' longer-term roadmap.

### zkSync Lite (Legacy)

zkSync Lite (formerly zkSync 1.0) was the first version of zkSync, launched in 2020. It focused primarily on scalable and low-cost token transfers and atomic swaps.
It did not support general-purpose smart contracts like zkSync Era does. While still operational, the focus of development and the ecosystem has largely shifted to zkSync Era.
zkSync Lite demonstrated the viability of ZK-rollups for payments and helped pave the way for the more advanced zkEVM capabilities of Era.

## Comparative Analysis

zkSync Era is a leading ZK-Rollup, competing primarily with other ZK-EVM projects and Optimistic Rollups like [[Arbitrum]] and [[Optimism]].

| Feature              | zkSync Era                                          | Polygon zkEVM                                 | Arbitrum One                                    | Optimism Bedrock                                |
| -------------------- | --------------------------------------------------- | --------------------------------------------- | ----------------------------------------------- | ----------------------------------------------- |
| Technology           | ZK-Rollup (zk-SNARKs)                               | ZK-Rollup (zk-SNARKs)                         | Optimistic Rollup                               | Optimistic Rollup                               |
| EVM Compatibility    | EVM-compatible (Solidity/Vyper via LLVM)            | High (EVM-equivalent, Type 2 goal)            | High (EVM-equivalent)                           | High (EVM-equivalent)                           |
| Key Differentiator   | Native Account Abstraction, LLVM Compiler, zkPorter | EVM-equivalence focus, part of Polygon 2.0    | Nitro performance, Stylus multi-language VM     | OP Stack, Superchain vision, RetroPGF           |
| Data Availability    | On-chain (Ethereum), zkPorter (future off-chain)    | On-chain (Ethereum)                           | On-chain (Ethereum)                             | On-chain (Ethereum)                             |
| Finality             | Fast (after ZK proof submission)                    | Fast (after ZK proof submission)              | Slower (7-day challenge period for withdrawals) | Slower (7-day challenge period for withdrawals) |
| Smart Contract Lang. | Solidity, Vyper (more via LLVM in future)           | Solidity, EVM languages                       | Solidity, EVM languages (more via Stylus)       | Solidity, EVM languages                         |
| Native Token         | ETH (for gas), future token expected for governance | ETH (for gas), MATIC (for sequencing/staking) | ETH (for gas), ARB (Governance)                 | ETH (for gas), OP (Governance)                  |
| Maturity             | Mainnet Alpha, growing rapidly                      | Mainnet Beta, growing                         | Well-established, large ecosystem               | Well-established, growing ecosystem             |

zkSync Era distinguishes itself with its deep commitment to Account Abstraction at the protocol level, which is a significant UX improvement. Its LLVM-based compiler infrastructure is also a forward-looking approach to language support. The potential of zkPorter for ultra-low-cost transactions (with different security trade-offs) is another unique aspect. While [[Polygon|Polygon zkEVM]] aims for closer EVM-equivalence, zkSync's approach through its custom zkEVM and compiler offers flexibility and unique features. Compared to Optimistic Rollups, zkSync offers faster finality due to the nature of ZK proofs.

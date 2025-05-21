#show-card

## Overview

Optimism is a prominent [[Layer 2]] scaling solution for [[Ethereum]], designed to significantly increase its transaction throughput and reduce costs while maintaining the security of the Ethereum mainnet. It utilizes Optimistic Rollup technology, similar to [[Arbitrum]], by processing transactions off-chain and then posting them in batches to Ethereum. The Optimism Collective is a key part of its ecosystem, focused on governing the network and funding public goods.

The core mission of Optimism is to scale Ethereum's technology and values. It addresses the problem of network congestion and high gas fees on Ethereum, which can make dApps slow and expensive to use. Optimism aims to provide a fast, stable, and scalable [[Layer 2]] blockchain that is economically sustainable and built as a public good.

A unique benefit of Optimism is its strong commitment to public goods funding, exemplified by its Retroactive Public Goods Funding (RetroPGF) program. Its key differentiators include the OP Stack, an open-source development stack that allows for the creation of custom L2 chains (OP Chains) forming a "Superchain" ecosystem, and its governance model centered around the Optimism Collective with its bicameral (Token House and Citizens' House) system.

Optimism was initially developed by Plasma Group, which later became Optimism PBC (Public Benefit Corporation) and then the Optimism Foundation. Key figures include Jinglan Wang, Karl Floersch, and Kevin Ho. Major milestones include the launch of its mainnet, the significant "Bedrock" upgrade which made it more EVM-equivalent and reduced costs, the introduction of the OP token for governance, and the ongoing development of the Superchain vision.

### Get Started with Optimism

| Resource            | Link                                                                         | Description                                                              |
| ------------------- | ---------------------------------------------------------------------------- | ------------------------------------------------------------------------ |
| Official Website    | [https://www.optimism.io/](https://www.optimism.io/)                         | Main website for Optimism and the Optimism Collective.                   |
| Optimism Foundation | [https://optimism.foundation/](https://optimism.foundation/)                 | The non-profit organization dedicated to growing the Optimism ecosystem. |
| Developer Docs      | [https://docs.optimism.io/](https://docs.optimism.io/)                       | Comprehensive documentation for developers.                              |
| Bridge              | [https://app.optimism.io/bridge](https://app.optimism.io/bridge)             | Official bridge to transfer assets between Ethereum and Optimism.        |
| Block Explorer      | [https://optimistic.etherscan.io/](https://optimistic.etherscan.io/)         | Optimism Mainnet block explorer.                                         |
| GitHub              | [https://github.com/ethereum-optimism](https://github.com/ethereum-optimism) | Source code and repositories for Optimism.                               |
| Community (Forum)   | [https://gov.optimism.io/](https://gov.optimism.io/)                         | Governance forum for discussions and proposals.                          |
| Discord             | [https://discord.gg/optimism](https://discord.gg/optimism)                   | Official Discord server for community and support.                       |
| Twitter             | [https://twitter.com/optimismFND](https://twitter.com/optimismFND)           | Official Twitter account for news and updates.                           |

## Key Services/Features

### Optimism Mainnet (Bedrock)

The Optimism Mainnet is the primary [[Layer 2]] chain that provides a scalable and low-cost environment for [[Ethereum]] dApps. Following the Bedrock upgrade, it became highly EVM-equivalent, making it very easy for developers to deploy existing Ethereum applications with minimal to no code changes.
The underlying technology is an Optimistic Rollup. Transactions are executed on Optimism, batched, and submitted to Ethereum. Like other optimistic systems, transactions are assumed valid unless challenged via a fraud-proof mechanism during a dispute window. The Bedrock upgrade significantly reduced transaction costs by optimizing data submission to L1 and improved node performance. It also introduced support for EIP-1559.
Real-world use cases span the entire DeFi ecosystem (e.g., Uniswap, Synthetix, Aave), NFT projects, and various other dApps looking for lower fees and faster transactions than [[Ethereum]] L1. Official documentation is available at [docs.optimism.io](https://docs.optimism.io/).

### The OP Stack

The OP Stack is a standardized, open-source development stack that powers Optimism. It's a modular blueprint for building highly scalable and interoperable [[Layer 2]] blockchains, known as OP Chains. The goal is to create a "Superchain" – a network of L2s built on the OP Stack that can communicate seamlessly, share security, and contribute to a unified ecosystem.
The technology abstracts various components of a blockchain (like sequencing, data availability, execution) into interchangeable modules. This allows developers to customize their OP Chains for specific needs while inheriting security from [[Ethereum]] and benefiting from shared upgrades and infrastructure. Key components include a modified version of Geth (op-geth) and a rollup node (op-node).
The OP Stack enables projects like Base (by Coinbase), Zora Network, and others to launch their own L2s, fostering a diverse and interconnected ecosystem. It aims to make deploying a rollup as easy as deploying a smart contract. Detailed information can be found in the [OP Stack documentation](https://stack.optimism.io/).

### Retroactive Public Goods Funding (RetroPGF)

Retroactive Public Goods Funding is a core component of Optimism's philosophy and economic model. It's a system for funding public goods that have already demonstrated value and impact within the Optimism ecosystem and the broader Ethereum community.
The mechanism involves rounds of funding where OP token holders and/or designated "badgeholders" vote to allocate funds to projects, developers, and contributors who have provided public goods. This incentivizes the creation of useful open-source software, infrastructure, education, and community resources without requiring upfront grants or specific deliverables, rewarding proven impact instead.
RetroPGF aims to create a sustainable funding model for the essential but often underfunded building blocks of the Web3 space. It fosters a positive-sum environment where contributing to the ecosystem is directly rewarded. More information can be found on the [Optimism website's section on RetroPGF](https://www.optimism.io/retropgf).

### Optimism Collective and Governance

The Optimism Collective is the governance body for the Optimism network. It's designed to be a grand experiment in digital democratic governance. The Collective is responsible for managing network parameters, allocating treasury funds, and stewarding the growth of the ecosystem.
It operates through a bicameral system:

1.  The Token House: Composed of OP token holders, responsible for project incentives, upgrades, and treasury allocations.
2.  The Citizens' House: Composed of individuals who earn "citizenship" through contributions, responsible for allocating RetroPGF.
    This dual structure aims to balance the interests of token holders with the broader values and public goods needs of the ecosystem. Governance discussions and proposals happen on the [Optimism Governance Forum](https://gov.optimism.io/).

## Comparative Analysis

Optimism, like [[Arbitrum]], is a leading Optimistic Rollup [[Layer 2]] solution for [[Ethereum]]. They share many similarities in their core technology and goals but differ in their specific implementations, ecosystem strategies, and governance philosophies.

| Feature            | Optimism (Bedrock)                                   | Arbitrum (One/Nitro)                                 |
| ------------------ | ---------------------------------------------------- | ---------------------------------------------------- |
| Technology         | Optimistic Rollup                                    | Optimistic Rollup                                    |
| EVM Compatibility  | High (EVM-equivalent)                                | High (EVM-equivalent with Nitro)                     |
| Fraud Proofs       | Single-round proofs (initially, evolving)            | Interactive, multi-round proofs                      |
| Development Stack  | OP Stack (modular, for Superchain)                   | Arbitrum Orbit (for L3s), Stylus (multi-language VM) |
| Ecosystem Vision   | Superchain (interoperable L2s)                       | Network of L2s and L3s                               |
| Public Goods Focus | Strong (RetroPGF, Collective)                        | Growing, via DAO and foundation initiatives          |
| Governance         | Bicameral (Token House, Citizens' House)             | DAO (ARB token holders)                              |
| Native Token       | OP (Governance, utility in Superchain)               | ARB (Governance)                                     |
| Key Differentiator | OP Stack, Superchain vision, RetroPGF, simple proofs | Nitro performance, Stylus, mature tech, Orbit L3s    |

Optimism's Bedrock upgrade brought it closer to EVM-equivalence and significantly improved performance and cost-efficiency. Its focus on the OP Stack and the Superchain concept represents a vision for a horizontally scalable network of L2s. The strong emphasis on RetroPGF is a defining characteristic of its economic and community model. Arbitrum, while also supporting ecosystem growth, has focused on technological advancements like Stylus for multi-language support and Orbit for L3s. Both are mature and highly adopted platforms, offering developers and users strong alternatives for scaling Ethereum.

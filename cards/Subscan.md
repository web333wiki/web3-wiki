#show-card

## Overview

Subscan is a high-precision, multi-chain block explorer widely used within the Web3 ecosystem, with a primary focus on [[Substrate]]-based networks like [[Polkadot]] and Kusama, and increasingly, [[EVM]]-compatible chains. It offers a comprehensive "Explorer as a Service" (EaaS) solution, providing users and developers with tools to explore, analyze, and understand on-chain data across a multitude of blockchain networks.

**Problem Solved:** Navigating and interpreting blockchain data can be complex. Subscan addresses this by providing a user-friendly, aggregated interface for real-time data, analytics, and smart contract exploration across nearly 100 networks. It simplifies the process of tracking transactions, examining blocks, monitoring addresses, and understanding network activity.

**Value Proposition:**

- **High-Precision Data:** Delivers accurate and detailed blockchain information.
- **Multi-Chain Support:** Extensive support for Substrate-based chains and a growing list of EVM networks.
- **Explorer as a Service (EaaS):** Offers a robust platform for developers and projects needing explorer functionalities.
- **User-Friendly Interface:** Designed for ease of use for both technical and non-technical users.

**Official Website:** [Subscan.io](mdc:https://www.subscan.io/)

**Status & Roadmap:** Subscan is live and actively maintained, continually expanding its support for new networks. It currently supports nearly 100 networks within the Polkadot ecosystem and beyond.

## Key Services/Features

Subscan provides a rich set of features for interacting with blockchain data:

- **Block Exploration:** Detailed views of individual blocks, including their contents, extrinsic, events, and parent hash.
- **Transaction (Extrinsic) Exploration:** In-depth information about specific transactions (or extrinsics in Substrate terminology), including sender, receiver, value, status, and associated events.
- **Address Tracking:** Ability to view balances, transaction history, and related on-chain activities for any given address.
- **[[Smart Contract]] Interaction:** For supported EVM chains, users can view contract details, read contract state, and sometimes interact with contract functions.
- **Network Analytics:** Provides statistics and charts on network activity, such as transaction volume, active accounts, and staking information.
- **Cross-Network Support:** Seamlessly switch between different supported blockchains from a unified interface.
- **API Services:** Offers APIs for developers to integrate Subscan's data into their own applications and services.
- **Governance Exploration:** Tools to view and track on-chain governance proposals, referenda, and voting activity on supported chains like Polkadot and Kusama.
- **Staking Dashboard:** Detailed information about validators, nominators, staking rewards, and other staking-related data for Proof-of-Stake networks.

## Technology

- **Blockchain/Platform:** Primarily built for [[Substrate]]-based blockchains, including major networks like [[Polkadot]], Kusama, Acala, Moonbeam, and Astar. It also offers robust support for various [[EVM]]-compatible chains.
- **Architecture:** Subscan operates on an "Explorer as a Service" (EaaS) model. This involves sophisticated data indexing nodes for each supported chain, which collect, process, and store blockchain data. This data is then made available through its web interface and API.
- **Core Mechanism(s):** The core of Subscan involves:
  - **Data Indexing:** Efficiently retrieving and indexing vast amounts of data from multiple heterogeneous blockchain networks.
  - **Data Aggregation & Presentation:** Consolidating data and presenting it in a structured, human-readable format.
  - **API Provisioning:** Exposing processed blockchain data through a set of APIs for third-party use.

## Ecosystem & Use Cases

- **Target Audience:**
  - **Users:** Individuals interacting with supported blockchains for checking transaction statuses, managing assets, or participating in governance.
  - **Developers:** Building dApps or services that require access to reliable on-chain data.
  - **Researchers & Analysts:** Studying blockchain activity, network health, and tokenomics.
  - **Projects & Teams:** Monitoring their own network or smart contracts, and providing an explorer for their user base.
- **How it's Used (Detailed Use Cases):**
  - **Transaction Verification:** Confirming if a transaction has been included in a block and its final status.
  - **Account Monitoring:** Tracking token balances and transaction history for specific wallet addresses.
  - **[[Smart Contract]] Auditing (Preliminary):** Inspecting deployed smart contract code (if verified) and transaction interactions.
  - **Network Health Check:** Observing block production, transaction throughput, and active validator sets.
  - **Staking Management:** Researching validators and tracking staking rewards.
  - **Governance Participation:** Following proposals and understanding voting outcomes.
- **Integrations:** Many projects within the [[Polkadot]] and Kusama ecosystems recommend or directly integrate Subscan as their preferred block explorer. For example, parachain projects often guide their users to Subscan for exploring their specific chain data.

## Getting Started & Resources

- **Accessing Subscan:**
  - Navigate to the main portal: [https://www.subscan.io/](mdc:https://www.subscan.io/)
  - Select your desired network from the dropdown list or by visiting a network-specific subdomain (e.g., `https://polkadot.subscan.io/`).
- **Documentation:** While a centralized documentation portal isn't prominently featured, usage is generally intuitive. API documentation is available for developers.
- **Community Channels & Support:**
  - Support is often provided through community channels of the respective blockchains Subscan supports.
  - Issues or feature requests can sometimes be raised via their GitHub.
- **Source Code:** Parts of Subscan's infrastructure are open-source.
  - **Subscan Essentials GitHub:** [subscan-explorer/subscan-essentials](mdc:https://github.com/subscan-explorer/subscan-essentials) (A scaffold project for Substrate explorers)

## Team and Project History

Subscan is developed and maintained by the Subscan team, known for their expertise in blockchain data indexing and explorer services. They have established themselves as a key infrastructure provider in the Substrate ecosystem. While specific team member details are not always prominent, their work is widely recognized. The project has evolved to support an increasing number of networks since its inception, driven by the growth of the Polkadot and broader Web3 space.

## Comparative Analysis

- **[[Etherscan]]**: The leading block explorer for [[Ethereum]] and EVM chains. Subscan provides similar functionality but with a broader focus that includes the Substrate ecosystem.
- **Polkadot.js Apps**: A powerful tool for interacting with [[Substrate]]-based chains, offering explorer features. However, Polkadot.js is often more developer-centric, while Subscan aims for a more user-friendly experience for a wider audience.
- **Other Chain-Specific Explorers (e.g., Solscan for [[Solana]], Tronscan for TRON):** Many L1 blockchains have their own dedicated explorers. Subscan's strength lies in its multi-chain aggregation, particularly for the interconnected [[Polkadot]] ecosystem.

Subscan differentiates itself through its specialized focus on the Substrate ecosystem, its "Explorer as a Service" model, and its commitment to providing high-precision data across a large and growing number of networks.
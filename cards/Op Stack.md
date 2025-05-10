#explain-card

## Introduction

- **Brief overview:** The OP Stack is a standardized, shared, and open-source development stack that powers [[Optimism]] and its broader ecosystem, including the vision for a "Superchain" of interoperable Layer 2 (L2) blockchains. It is maintained by the Optimism Collective.
- **Importance in Web3:** The OP Stack aims to simplify the creation of new L2 blockchains by providing a common set of tools and components. This promotes collaboration, reduces redundant work, and fosters a more interconnected and scalable Ethereum ecosystem.
- **Basic definition:** A collection of software components (like consensus, execution, and sequencing modules) that can be assembled to build customized L2 rollups, primarily focused on Optimistic Rollups.
- **Official Resource:** [OP Stack Documentation](https://docs.optimism.io/stack/getting-started)

## Core Concepts

- **Modularity:** The OP Stack is designed to be modular, allowing developers to potentially customize or replace different components (e.g., data availability layer, execution layer) to suit specific needs, although current iterations like Bedrock are more tightly coupled for production readiness.
- **Standardization:** By providing a standard blueprint for L2s, the OP Stack facilitates interoperability between chains built with it, contributing to the Superchain concept where chains can communicate and share security more seamlessly.
- **Optimistic Rollups:** The current focus of the OP Stack is on building Optimistic Rollups, which assume transactions are valid by default and use fraud proofs to resolve disputes, thereby scaling Ethereum by processing transactions off-chain.
- **Bedrock Upgrade:** Bedrock is a significant iteration of the OP Stack, offering lower fees, faster deposits/withdrawals, and improved modularity. It serves as the foundation for current OP Stack based chains like OP Mainnet.
- **Superchain Vision:** The OP Stack is a key enabler of the Superchain, a proposed network of L2s that share security, communication layers, and the OP Stack itself, aiming to create a horizontally scalable and cohesive blockchain ecosystem.

## Use Cases

- **Building Custom L2 Rollups:** The primary use case is for developer teams to launch their own Optimistic Rollup L2 chains tailored to specific applications or communities (e.g., Base, Zora Network).
- **Powering OP Mainnet:** The OP Stack is the underlying technology for OP Mainnet, one of the leading Ethereum L2 scaling solutions.
- **Experimentation and Research:** While an official, production-ready version like Bedrock is recommended for mainnet deployments, the open-source nature of the OP Stack allows for experimentation with different L2 designs and configurations.
- **Enhancing Interoperability:** Chains built on the OP Stack are designed to be more easily interoperable, paving the way for smoother cross-chain communication and asset transfers within the Superchain.

## Related Concepts (Optional)

- [[Optimism]]
- [[Layer 2]]
- [[Rollup]]

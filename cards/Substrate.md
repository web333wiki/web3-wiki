#explain-card

## Introduction

- **Brief overview:** Substrate is a modular and extensible open-source framework for building custom blockchains. Developed by Parity Technologies, it provides the core components necessary to create a blockchain, allowing developers to focus on the unique logic and features of their specific application.
- **Importance in Web3:** Substrate significantly lowers the barrier to blockchain development, enabling teams to create highly customized and optimized blockchains (parachains, parathreads, or solo chains) tailored to specific use cases. It is the foundational technology behind Polkadot and Kusama, fostering an ecosystem of interoperable blockchains.
- **Basic definition:** A software development kit (SDK) that provides the building blocks for creating new Layer-1 blockchains or parachains.

## Core Concepts

- **FRAME (Framework for Runtime Aggregation of Modularized Entities):** A powerful system for building blockchain runtimes (the state transition logic) by composing modules called "pallets." Pallets are reusable pieces of logic for common blockchain functionalities (e.g., staking, governance, assets).
- **Wasm (WebAssembly) Runtime:** Substrate blockchains can have their runtime logic compiled to Wasm. This allows for forkless runtime upgrades, meaning the blockchain's logic can be updated without requiring a hard fork, by deploying a new Wasm binary on-chain.
- **Node Template:** Substrate provides a node template that serves as a starting point for building a new blockchain. It includes networking, consensus, and a basic runtime.
- **Consensus Agnostic:** While Substrate comes with built-in consensus mechanisms like BABE and GRANDPA (used by Polkadot), it is designed to be consensus-agnostic, allowing developers to integrate other consensus algorithms.
- **Customizable Pallets:** Developers can create custom pallets to implement unique features for their blockchain, or use a library of pre-built open-source pallets.

## Use Cases

- **[[Polkadot]] and [[Kusama]] Network:** Substrate is the core framework used to build Polkadot, Kusama, and their respective parachains.
- **Application-Specific Blockchains:** Projects can build entire blockchains specifically designed for their application needs, such as DeFi, gaming, identity, or supply chain solutions.
- **Private/Consortium Chains:** Substrate can be used to create permissioned blockchains for enterprise use cases.
- **Rapid Prototyping:** Enables quick iteration and development of blockchain concepts.

## Related Concepts (Optional)

- [[Polkadot]]
- [[Kusama]]
- [[Parachain]]
- [[Blockchain Framework]]
- [[WebAssembly (Wasm)]]
- [[Forkless Runtime Upgrade]]

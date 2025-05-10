#explain-card

## Introduction

Substrate is a modular and extensible open-source framework for building custom blockchains, developed by Parity Technologies. It provides the core components necessary to create a blockchain, allowing developers to focus on the unique logic and features of their specific application. You can find more information at the [official Substrate documentation](https://docs.substrate.io/).

Substrate significantly lowers the barrier to blockchain development. It enables teams to create highly customized and optimized blockchains—such as parachains, parathreads, or solo chains—tailored to specific use cases. As the foundational technology behind [[Polkadot]], Substrate fosters an ecosystem of interoperable blockchains, making it a crucial software development kit (SDK) for creating new Layer-1 blockchains or parachains.

## Core Concepts

Substrate's architecture is built around several core concepts that provide its flexibility and power:

- **FRAME (Framework for Runtime Aggregation of Modularized Entities):** This is a powerful system for building blockchain runtimes (the state transition logic) by composing modules called "pallets." Pallets are reusable pieces of logic for common blockchain functionalities like staking, governance, and assets, allowing for modular development.

- **Wasm (WebAssembly) Runtime:** A key feature of Substrate is that blockchain runtimes can be compiled to WebAssembly (Wasm). This enables forkless runtime upgrades, meaning the blockchain's core logic can be updated by deploying a new Wasm binary on-chain, without requiring a disruptive hard fork.

- **Node Template & Consensus Agnosticism:** Substrate provides a node template as a starting point, which includes networking, consensus, and a basic runtime. While it comes with built-in consensus mechanisms like BABE and GRANDPA (used by Polkadot), Substrate is designed to be consensus-agnostic, allowing developers to integrate other consensus algorithms if needed.

- **Customizable Pallets:** Beyond the standard set, developers have the freedom to create custom pallets to implement unique features specific to their blockchain, or they can leverage a growing library of pre-built open-source pallets from the community.

## Use Cases

Substrate's versatility makes it suitable for a wide range of applications:

- It serves as the core framework for the [[Polkadot]] network and its parachains, as well as the Kusama network.
- Teams can build **application-specific blockchains** tailored for diverse needs such as DeFi, gaming, digital identity, or supply chain management.
- It can be used to create **private or consortium chains** for enterprise solutions requiring permissioned access.
- The framework facilitates **rapid prototyping**, allowing for quick iteration and development of new blockchain concepts.

## Related Concepts (Optional)

- [[Polkadot]]
- [[Parachain]]

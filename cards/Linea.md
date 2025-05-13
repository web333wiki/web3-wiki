#show-card

## Overview

Linea is a Layer 2 (L2) scaling solution for Ethereum, developed by ConsenSys. It aims to provide a developer-friendly, EVM-equivalent environment with significantly lower transaction costs and faster throughput than Ethereum Layer 1. Linea utilizes zk-Rollup technology, specifically a type of zkEVM, to achieve its scalability and security goals.

- **Problem Solved:** High gas fees and limited throughput on Ethereum L1, making it difficult for some applications to scale and for users to transact affordably.
- **Value Proposition:** Offers EVM equivalence (making it easy to migrate existing Ethereum dApps), the security benefits of zk-Rollups (cryptographic validity proofs), and backing from ConsenSys, a major Ethereum development company.
- **Official Website:** [https://linea.build/](https://linea.build/)
- **Status:** Live on mainnet.

## Key Features

- **zk-Rollup (zkEVM Type 2):** Bundles transactions off-chain and generates cryptographic proofs (validity proofs, specifically ZK-SNARKs) to attest to their correctness on Ethereum L1. Aims for a high degree of EVM compatibility.
- **EVM Equivalence:** Designed to allow developers to deploy existing Solidity smart contracts and use familiar Ethereum tooling with minimal changes.
- **ConsenSys Ecosystem Integration:** Benefits from ConsenSys's suite of developer tools and infrastructure, including MetaMask, Infura, and Truffle.
- **Focus on Developer Experience:** Prioritizes ease of use and seamless migration for Ethereum developers.
- **Quantum-Resistant Cryptography:** Linea uses the Vortex ZK-proof system, which employs lattice-based cryptography for its prover, aiming for future-proofing against quantum computing threats.

## Technology

- **Blockchain/Platform:** Layer 2 zk-Rollup built on [[Ethereum]].
- **Architecture:** Sequencer orders and batches transactions, a prover generates validity proofs for these batches, and these proofs are submitted to Ethereum L1 for verification.
- **Core Mechanism:** zkEVM (Zero-Knowledge Ethereum Virtual Machine) that executes smart contracts compatibly with the EVM and uses ZK-SNARKs for proofs.

## Ecosystem & Use Cases

- **Target Audience:** Ethereum developers, dApps seeking scalability, DeFi users, NFT projects.
- **How It's Used:** Deployment of a wide range of dApps, including DeFi, NFTs, gaming, and social applications, benefiting from lower fees and faster transactions.

## Getting Started & Resources

- **Access:** Users can interact with Linea by adding the Linea Mainnet network to EVM-compatible wallets and using bridges to transfer assets.
- **Documentation:** [https://docs.linea.build/](https://docs.linea.build/)
- **Community:** Active on Discord, Twitter, and other social channels.
- **Bridge:** [https://bridge.linea.build/](https://bridge.linea.build/)

## Related Concepts

- [[Ethereum]]
- [[Layer 2 Rollups]] (or [[Rollup]])
- [[zk-Rollups]]
- [[zkEVM]]
- [[EVM]]
- [[ConsenSys]] (if a card is made)

#explain-card

## Overview

The **Beacon Chain** is a foundational component of Ethereum's Proof of Stake (PoS) consensus mechanism. Launched on December 1, 2020, it initially ran separately from the Ethereum mainnet (which was then using Proof of Work). The Beacon Chain introduced the consensus logic for PoS, managed the registry of validators, and applied the consensus rules. Its primary role was to coordinate and attest to the state of shard chains (though full sharding was later deprioritized in favor of rollup-centric scaling) and, most importantly, to serve as the new consensus layer for Ethereum after [[The Merge]].

- **Problem Solved:** Provided the PoS consensus mechanism for Ethereum, enabling a shift away from the energy-intensive Proof of Work model. It laid the groundwork for a more scalable and sustainable Ethereum.
- **Value Proposition:** Manages validators, processes attestations and block proposals, and ensures the security and liveness of the Ethereum network under PoS.
- **Status:** Live and fully integrated as Ethereum's consensus layer since [[The Merge]] in September 2022.

## Key Features & Functionality

- **Validator Management:** Maintains the set of active validators, processes their deposits and exits, and assigns them duties (proposing blocks, attesting to blocks).
- **Attestations and Aggregation:** Validators submit attestations (votes) for blocks they deem valid. The Beacon Chain aggregates these attestations to achieve consensus.
- **Block Proposal:** Selects validators to propose new blocks for the Ethereum network.
- **Fork Choice Rule (LMD GHOST):** Implements the logic by which the canonical chain is identified, based on the accumulated weight of attestations.
- **Randomness Generation (RANDAO):** Provides a source of pseudo-randomness used for selecting block proposers and committees.
- **Crosslinks (Initially for Sharding):** Designed to validate and include the state of shard chains (this aspect evolved as the sharding roadmap changed).
- **Synchronization with Execution Layer:** After [[The Merge]], the Beacon Chain provides the consensus (who proposes the next block, what is the canonical chain) while the execution layer (formerly mainnet) processes transactions and smart contracts.

## Role in The Merge

[[The Merge]] was the event where the original Ethereum mainnet (execution layer) officially adopted the Beacon Chain as its engine for consensus. Instead of miners validating blocks through PoW, the Beacon Chain's PoS validators took over this role. The execution layer listens to the Beacon Chain for instructions on which blocks are canonical and executes the transactions within them.

## Related Concepts

- [[Proof of stake]]
- [[The Merge]]
- [[Validator]]
- [[Staking]]
- [[Ethereum]]

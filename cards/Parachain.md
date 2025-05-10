#explain-card

## Introduction

- **Brief overview:** A parachain, short for "parallelized chain," is an application-specific blockchain that connects to and is secured by a central Relay Chain, most notably [[Polkadot]]'s Relay Chain or [[Kusama]]'s Relay Chain.
- **Importance in Web3:** Parachains enable scalability and specialization within a larger blockchain ecosystem. They allow diverse blockchains with unique features and optimizations to coexist and interoperate while benefiting from the shared security of the Relay Chain.
- **Basic definition:** A Layer-1 blockchain that runs in parallel with other parachains, connected to and validated by a Layer-0 Relay Chain, forming a sharded network.

## Core Concepts

- **Relay Chain Connection:** Parachains lease a slot on the Relay Chain (e.g., through auctions on Polkadot/Kusama) to connect. Once connected, their blocks are validated by the Relay Chain's validators.
- **Shared Security:** Parachains inherit their security from the Relay Chain. This means they don't need to bootstrap their own validator set, significantly lowering the barrier to creating a secure blockchain.
- **Specialization:** Each parachain can be optimized for a specific use case (e.g., DeFi, NFTs, identity, smart contracts in a specific language like EVM or Wasm). They can have their own governance, native tokens, and runtime logic tailored to their purpose.
- **Interoperability (XCM):** Parachains within the same ecosystem (e.g., Polkadot) can communicate and exchange assets or arbitrary messages with each other using Cross-Consensus Message Format (XCM). This allows for rich cross-chain interactions.
- **Collators:** Parachain maintainers, known as collators, are responsible for producing new block candidates for their parachain and submitting them to the Relay Chain validators for inclusion and finalization.
- **Governance:** While security is shared, parachains typically maintain their own governance mechanisms for protocol upgrades and decision-making specific to their chain.

## Use Cases

- **Application-Specific Blockchains:** Building a blockchain optimized for a particular dApp or service (e.g., a DeFi-specific chain like Acala, an EVM-compatible smart contract platform like Moonbeam).
- **Ecosystem Hubs:** Parachains that act as hubs for specific functionalities, like smart contract execution, asset issuance, or bridging to other networks.
- **Consortium Chains:** Private or permissioned blockchains that connect to a public Relay Chain for security and interoperability.
- **Experimentation (on Kusama):** Parachains on Kusama often serve as a proving ground for new technologies and economic models before potential deployment on Polkadot.

## Related Concepts (Optional)

- [[Polkadot]]
- [[Substrate]] (often used to build parachains)

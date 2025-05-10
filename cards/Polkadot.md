#show-card

## Project Overview

Polkadot is a next-generation blockchain protocol designed to enable scalability, interoperability, and innovation by connecting multiple specialized blockchains (called parachains) into a single unified network. It was founded by Dr. Gavin Wood, co-founder of Ethereum, and is developed by the Web3 Foundation.

Its core purpose is to overcome the limitations of isolated blockchains by providing a shared security model (via its Relay Chain) and a framework for seamless cross-chain communication (XCM - Cross-Consensus Message Format). Key features include its sharded parachain architecture, on-chain governance, forkless upgrades, and the [[Substrate]] framework for building custom blockchains.

Discover more at the [official Polkadot website](https://polkadot.network/).

## Technical Details

- **Underlying Technology:** Polkadot uses a Nominated Proof-of-Stake (NPoS) consensus mechanism for its Relay Chain. The Relay Chain doesn't handle smart contracts directly but is responsible for coordinating the network, including security and consensus for connected parachains.
- **Architecture Overview:**
  - **Relay Chain:** The heart of Polkadot, providing security and consensus to the network.
  - **[[Parachain|Parachains]]:** Sovereign blockchains with their own logic, tokenomics, and governance, which connect to the Relay Chain for shared security and interoperability.
  - **Parathreads:** Similar to parachains but with a pay-as-you-go model, suitable for projects not needing continuous connectivity.
  - **Bridges:** Connect Polkadot to external blockchains like Ethereum or Bitcoin.
- **Unique Selling Points:**
  - **Shared Security:** Parachains benefit from the economic security of the entire Polkadot network.
  - **Interoperability:** Enables different blockchains to communicate and exchange data/assets trustlessly.
  - **Customizability via [[Substrate]]:** Developers can build highly specialized blockchains tailored to specific use cases.
  - **Forkless Upgrades:** The network can upgrade its own runtime without requiring hard forks, facilitated by on-chain governance.
  - **On-Chain Governance:** A sophisticated governance system allows stakeholders to manage protocol upgrades, treasury funds, and other network parameters.

## Use Cases

- **DeFi Hubs:** Parachains dedicated to decentralized finance (e.g., Acala, Moonbeam often offering EVM compatibility).
- **NFT and Gaming Platforms:** Specialized parachains for NFTs, gaming, and metaverse applications.
- **Identity Solutions:** Blockchains focused on decentralized identity and credentialing.
- **IoT and Supply Chain:** Parachains designed for Internet of Things (IoT) data or supply chain management.
- **Cross-Chain Bridges and Services:** Enabling communication and asset transfer between Polkadot and other ecosystems.

## Getting Started

- **How to use/access:** Users interact with Polkadot and its native token (DOT) via wallets like Polkadot.js, Fearless Wallet, Nova Wallet, or hardware wallets. DOT is used for staking, governance, and parachain auctions/leases.
- **Official Resources:**
  - Website: [Polkadot Network](https://polkadot.network/)
  - Wiki: [Polkadot Wiki](https://wiki.polkadot.network/)
  - Polkadot.js Apps: [Polkadot JS](https://polkadot.js.org/apps/)
  - Explorer: [Subscan](https://polkadot.subscan.io/), [Polkastats](https://polkastats.io/)
- **Community:** Active on various channels including the Polkadot Forum, Discord, Reddit (r/dot), and Telegram.

## Related Links (Optional)

- [[Substrate]]
- [[Parachain]]
- [[Proof of stake]]

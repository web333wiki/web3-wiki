#show-card

## Project Overview

### Summary

Berachain is an [[EVM]]-compatible [[Layer 1]] blockchain that introduces a tri-token economic model designed to enhance liquidity, staking, and governance. Its core mission is to address common challenges in [[Decentralized finance]], such as fragmented liquidity and misaligned incentives between stakers and protocols. It seeks to solve the problem of capital inefficiency and mercenary liquidity often seen in other blockchain ecosystems by deeply integrating liquidity provision into the consensus layer.

### Unique Benefits and Differentiators

Berachain's primary differentiator is its Proof-of-Liquidity (PoL) consensus mechanism. Unlike traditional Proof-of-Stake systems where users stake the native gas token, PoL allows users to stake various blue-chip assets (like BTC, [[Ethereum]], [[Stablecoin]]s) into Berachain [[Validator]]s. In return, users receive BGT (Berachain Governance Token) which can be used for governance or delegated to [[Validator]]s to earn a share of network fees and block rewards in HONEY (Berachain's native [[Stablecoin]]). This mechanism aims to:

- Attract and retain deep liquidity within the ecosystem.
- Align incentives between LPs, dApps, and [[Validator]]s.
- Create a more robust and capital-efficient environment for [[Decentralized finance]] applications.
  The tri-token model consists of:
- BERA: The gas token, used for transaction fees.
- BGT: The non-transferable governance token, earned by staking assets.
- HONEY: The native, over-collateralized [[Stablecoin]], minted by users.

### Background

Berachain was co-founded by Smokey The Bera, Papa Bear, and Dev Bear, who were previously active in the OlympusDAO community. The project emerged from discussions around improving [[Decentralized finance]] primitives and capital efficiency. Key milestones include the development of the Polaris EVM framework, the design of the Proof-of-Liquidity consensus, and the launch of its public testnet "Artio." The project has garnered significant attention and backing from prominent venture capital firms in the crypto space.

### Getting Started

| Resource            | Link                                           | Description                                                                 |
| ------------------- | ---------------------------------------------- | --------------------------------------------------------------------------- |
| Official Website    | `https://www.berachain.com/`                   | Main portal for information about Berachain.                                |
| Documentation       | `https://docs.berachain.com/`                  | Comprehensive guides, technical specifications, and developer resources.    |
| Blog / Updates      | `https://www.berachain.com/blog`               | Latest news, articles, and announcements from the Berachain team.           |
| Community (Discord) | `https://discord.gg/berachain`                 | Official Discord server for community discussions, support, and engagement. |
| GitHub              | `https://github.com/berachain`                 | Source code repositories for Berachain's core components and tools.         |
| Testnet Faucet      | (Link to specific testnet faucet if available) | For obtaining testnet BERA tokens to interact with the Artio testnet.       |

## Key Services/Features

### Proof-of-Liquidity (PoL) Consensus

Proof-of-Liquidity is Berachain's novel consensus mechanism. Users contribute liquidity by staking various assets (e.g., [[Ethereum]], BTC, [[Stablecoin]]s) into [[Validator]] vaults. This staked liquidity is then used within the Berachain ecosystem by native dApps, generating fees that are distributed back to stakers and [[Validator]]s. In return for staking, users receive BGT, the governance token. This system is designed to ensure deep, protocol-owned liquidity, align [[Validator]] incentives with ecosystem growth, and provide a sustainable yield for liquidity providers. The underlying technology leverages the Cosmos SDK and CometBFT (formerly Tendermint Core) for consensus, with modifications to integrate the PoL module. Real-world use cases include enhancing capital efficiency for [[Decentralized finance]] protocols built on Berachain, providing sustainable yields for LPs, and fostering a more cooperative relationship between the chain and its applications.

### Tri-Token Economic Model

Berachain utilizes a three-token system to manage its economy:

1.  BERA: This is the network's gas token, used to pay for transaction fees on the blockchain. It can be earned by validators and delegators.
2.  BGT (Berachain Governance Token): BGT is a non-transferable, soulbound token awarded to users who contribute to the Proof-of-Liquidity mechanism by staking assets. BGT holders can participate in network governance, such as voting on proposals, and can delegate their BGT to validators to earn a share of protocol fees and HONEY inflation. This design aims to ensure that governance power resides with those actively contributing to the network's security and liquidity.
3.  HONEY: This is Berachain's native, decentralized, over-collateralized [[Stablecoin]]. Users can mint HONEY by collateralizing accepted assets. HONEY serves as the primary medium of exchange within the Berachain [[Decentralized finance]] ecosystem and is used to pay rewards to BGT delegators.

This model aims to create a flywheel effect where increased liquidity leads to more HONEY minting, more dApp activity, more fees, and thus greater incentives to provide liquidity and participate in governance.

### EVM Compatibility (Polaris EVM)

Berachain is fully [[EVM]]-compatible through its Polaris EVM framework. This allows developers to easily deploy existing [[Ethereum]] [[Smart contract]]s and dApps onto Berachain with minimal or no code changes. The Polaris EVM is built as a module on top of the Cosmos SDK, combining the flexibility and interoperability of [[Cosmos]] with the familiarity and widespread adoption of the [[Ethereum]] Virtual Machine. This feature significantly lowers the barrier to entry for developers looking to build on Berachain, leveraging the extensive tooling and developer community of [[Ethereum]]. Use cases include porting popular [[Decentralized finance]] protocols, [[NFT]] projects, and other [[EVM]]-based applications to the Berachain ecosystem.

### Native Decentralized Applications (dApps)

While allowing external developers to build, Berachain also plans to launch a set of native dApps that are deeply integrated with the Proof-of-Liquidity mechanism. These may include:

- A native [[DEX]] (Decentralized Exchange) that utilizes the staked liquidity.
- A lending protocol for HONEY.
- A perpetuals trading platform.
  These native applications are intended to bootstrap the ecosystem, showcase the capabilities of PoL, and generate fees that contribute to the network's economic loop. The technology behind these dApps will leverage the Polaris EVM and integrate directly with the PoL module for liquidity access.

## Comparative Analysis

Berachain can be compared to other [[Layer 1]] blockchains, particularly those built using the Cosmos SDK or those focusing on [[Decentralized finance]] and liquidity solutions.

| Feature             | Berachain (Proof-of-Liquidity)                             | Typical Proof-of-Stake (e.g., [[Cosmos]] Hub, new L1s)         | [[Ethereum]] (Proof-of-Stake)          |
| ------------------- | ---------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------- |
| Consensus           | Proof-of-Liquidity                                         | Proof-of-Stake (Native Token Staking)                          | Proof-of-Stake (ETH Staking)           |
| Staked Assets       | Various blue-chip assets (BTC, ETH, [[Stablecoin]]s, etc.) | Primarily the native network token                             | ETH                                    |
| Liquidity Mechanism | Integrated into consensus; protocol-managed                | Relies on external dApps & LPs for liquidity                   | Relies on external dApps & LPs         |
| Native Stablecoin   | HONEY (over-collateralized)                                | Varies; often relies on bridged or third-party [[Stablecoin]]s | DAI, USDC, USDT (third-party)          |
| Governance Token    | BGT (non-transferable, earned via PoL)                     | Native network token (transferable)                            | Various dApp tokens; ETH for consensus |
| EVM Compatibility   | Yes (Polaris EVM)                                          | Often, or via solutions like Evmos                             | Native                                 |
| Capital Efficiency  | Aims for high capital efficiency via PoL                   | Can lead to capital silos if staked token isn't used           | Varies by dApp design                  |

Berachain's approach differs significantly by directly incentivizing and utilizing a broader range of staked assets for network security and liquidity, aiming to create a more symbiotic relationship between the chain and its applications. Other L1s like Sei Network also focus on specific [[Decentralized finance]] use cases (e.g., order books) but may not have as deeply integrated a liquidity consensus mechanism as Berachain proposes. Compared to [[Ethereum]], Berachain aims to provide a more capital-efficient and integrated [[Decentralized finance]] experience from the base layer.

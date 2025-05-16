#show-card

## Overview

Berachain is an [[EVM]]-compatible Layer 1 blockchain built on the Cosmos SDK. It utilizes a novel consensus mechanism called Proof of Liquidity (PoL) which aims to align network incentives, build strategic liquidity, and strengthen the network-level relationship between liquidity and security. Berachain features a tri-token system consisting of BERA (gas token), BGT (governance token), and HONEY (native consensus collateralized [[Stablecoin]]).

- **Official Website**: [Berachain](mdc:https://www.berachain.com/)
- **Status**: Public Testnet (Artio) as of early 2024. Mainnet launch anticipated.
- **Roadmap**: Details are typically shared through official channels like their blog and social media.

### Problem Solved

Berachain aims to address liquidity challenges in [[Decentralized finance]] by creating a system where liquidity provision is directly incentivized at the protocol level, thus improving capital efficiency and reducing reliance on mercenary capital. It also seeks to mitigate issues related to MEV (Maximal Extractable Value) and improve overall network security through its unique consensus mechanism.

### Value Proposition

- **Proof of Liquidity (PoL):** A novel consensus mechanism that aims to create a synergistic relationship between network security and liquidity provision. Users can stake blue-chip assets like [[Bitcoin]], [[Ethereum]], and stablecoins with validators to earn BGT, the governance token. Validators then direct BGT emissions to liquidity pools, incentivizing LPs.
- **Tri-Token System:**
  - **BERA:** The network's gas token, used for transaction fees.
  - **BGT (Berachain Governance Token):** A non-transferable (soulbound) token used for governance and earned by staking assets. BGT holders can vote on network parameters and direct BGT emissions to liquidity pools.
  - **HONEY:** A native, over-collateralized stablecoin pegged to USDC, minted by users against their collateral.
- **EVM Compatibility:** Allows for easy deployment of existing Ethereum-based applications and tools.
- **Modular Architecture (Cosmos SDK):** Provides flexibility and interoperability within the broader Cosmos ecosystem.

## Key Services/Features

- **Native Decentralized Exchange (DEX):** Berachain includes a native DEX that facilitates trading and liquidity provision for assets within its ecosystem.
- **Lending Protocol:** A native lending and borrowing protocol for HONEY and other assets.
- **Perpetuals Trading:** Functionality for decentralized perpetuals trading.
- **Governance:** BGT holders participate in on-chain governance, influencing the direction of the protocol and BGT emissions.

## Technology

- **Blockchain/Platform:** Built on the Cosmos SDK, providing Tendermint consensus and IBC (Inter-Blockchain Communication Protocol) compatibility. It is an EVM-identical Layer 1.
- **Consensus Mechanism:** Proof of Liquidity (PoL). This mechanism involves users delegating assets to validators. Validators produce blocks and direct BGT emissions to liquidity pools based on BGT holder votes. LPs in these incentivized pools earn BGT.
- **Core Mechanism(s):**
  - **Proof of Liquidity:** Integrates staking and liquidity provision. Stakers of blue-chip assets earn BGT, which is then used to incentivize liquidity in specific pools. This creates a feedback loop designed to attract and retain liquidity.
  - **Tri-Token Economy:** The interplay between BERA, BGT, and HONEY is central to the chain's economic model, aiming to balance incentives for security, liquidity, and utility.
- **Smart Contracts:** As an EVM-compatible chain, Berachain supports smart contracts written in [[Solidity]] and other EVM languages. Details on specific core contracts and audits are typically found in their official documentation and GitHub.

## Ecosystem & Use Cases

- **Target Audience:** DeFi users, developers looking for an EVM-compatible L1 with novel liquidity solutions, projects seeking to build with strong liquidity incentives.
- **How it's Used (Detailed Use Cases):**
  - Users can stake assets (e.g., ETH, BTC, stablecoins) to earn BGT.
  - BGT holders can vote to direct BGT emissions to specific liquidity pools on the native DEX.
  - Liquidity providers can add liquidity to incentivized pools to earn BGT rewards and trading fees.
  - Users can mint HONEY stablecoins by providing collateral.
  - Developers can deploy existing EVM dApps or build new ones on Berachain.
- **Integrations:** As a Cosmos SDK chain, it has the potential for IBC integrations. Specific dApp integrations are emerging, particularly during the testnet phase.
- **Tokenomics:**
  - **BERA:** Used for gas fees.
  - **BGT:** Governance token, earned via PoL staking, non-transferable. Used to vote on BGT emissions to LPs.
  - **HONEY:** Native stablecoin.
    Further details on supply, distribution, and emission schedules are typically found in official documentation.

## Getting Started & Resources

- **Accessing:** Interact with Berachain via its public testnet (Artio). Details on connecting a wallet (e.g., MetaMask) are usually provided in their documentation or community guides.
- **Comprehensive Documentation:** [Berachain Docs](mdc:https://docs.berachain.com/) (Official documentation often evolves, verify URL).
- **Community Channels:**
  - Discord: (Link usually found on their official website)
  - Twitter/X: [Berachain on X](mdc:https://twitter.com/berachain)
- **Source Code:** [Berachain GitHub](mdc:https://github.com/berachain)

## Team and Project History

Information about the core team is often pseudonymous, following a common trend in some crypto projects. The project has gained significant attention and backing from various venture capital firms.

- **Project History & Milestones:**
  - Emerged from a community known for the "Bong Bears" NFT collection.
  - Raised significant funding rounds.
  - Launched its public testnet "Artio" in early 2024.
  - Mainnet launch is anticipated.

## Comparative Analysis

- **Similar Projects:**
  - **Other EVM-compatible L1s:** Compares with chains like [[Ethereum]], [[Avalanche]], Fantom in terms of EVM compatibility and attracting dApps. Berachain differentiates itself with PoL and its tri-token model.
  - **Cosmos Ecosystem Chains:** Shares similarities with other Cosmos SDK chains due to its underlying technology, offering interoperability via IBC.
  - **Liquidity-focused Protocols:** Projects like Frax Finance (with its veFXS model influencing emissions) or OlympusDAO (with its bonding mechanism) have explored related concepts of protocol-owned or directed liquidity, though Berachain's PoL is a distinct L1 consensus approach.
- **Key Differentiators:**
  - Proof of Liquidity as a core consensus mechanism directly tying security to liquidity.
  - The tri-token model (BERA, BGT, HONEY) designed to create a balanced and incentivized ecosystem.
  - Strong community origins and engagement.
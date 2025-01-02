#show-card 

## Introduction

Solana is a high-performance blockchain designed for mass adoption. Compared to rival blockchains like [[Ethereum]], it offers super-fast 400ms confirmation times and low transaction fees, with a median fee of 0.00064 SOL per transaction. Solana aims to provide the best experience for developers and users to build and use decentralized applications.

## Technical Details

### Innovative Consensus Mechanism

Both Ethereum and Solana use a consensus mechanism called [[Proof of stake]] (PoS). Solana introduces an innovative global clock design called Proof of History (PoH), which arranges the sequence of blocks, transactions, and events. In the event of a fork, Solana can quickly resolve it using PoH, whereas Ethereum validators need to calculate attestations from the genesis block to the latest block, which is time-consuming.

### On-Chain Programs

In Solana, [[Smart Contract]]s are referred to as "on-chain programs" and are written in Rust. Each program is an on-chain account that stores executable logic, organized into specific functions called instructions. There is a framework called [Anchor](https://github.com/coral-xyz/anchor) that helps developers write, test, and deploy on-chain programs efficiently.

### Account Model
The most significant difference between Solana and Ethereum is the account model. In Ethereum, each account can be either an Externally Owned Account (EOA) or a Contract Account, where the contract logic and storage are tied together. In Solana, the contract account and storage account are separated, making contract accounts completely stateless.

## Applications

- [Explorer: Solscan](https://solscan.io/)
- [Explorer: Solana Explorer](https://explorer.solana.com/)
- [Explorer: SolanaFM](https://solana.fm/?cluster=mainnet-alpha)

## Social Media

- [Official Website](https://solana.com/)
- [Official Documentation](https://solana.com/docs)
- [Github](https://github.com/solana-foundation)
- [X](https://x.com/solana)
- [Youtube](https://www.youtube.com/SolanaFndn)

## Latest Updates

- 2023-04 Solana Mobile began selling in the Solana Saga, an Android smartphone with Solana-based dapps.
- 2020-03 Generated the first block on the Solana Mainnet
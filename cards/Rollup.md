#explain-card

## What is Rollup?

A **rollup** is a Layer 2 scaling solution for [[Ethereum]] that bundles or "rolls up" many transactions into a single batch, which is then posted to the Ethereum mainnet. Rollups execute transactions off-chain (on their own networks) but regularly submit transaction data to Ethereum, inheriting its security. Once data is posted to Ethereum, reverting a rollup transaction requires reverting the corresponding Ethereum transaction. This mechanism allows the transaction fee on Ethereum to be distributed among many rollup transactions, significantly reducing costs for users and increasing throughput.

## Types of Rollup

There are two main types of rollup solutions: **Optimistic Rollup** and **ZK Rollup**. They differ in how they verify off-chain transaction execution.

### Optimistic Rollup

Optimistic Rollup assumes transactions are valid by default. Transactions are executed off-chain, and the results are posted to Ethereum as calldata or, since the [[Dencun Upgrade (EIP-4844)]], as blobs (see below). Optimistic rollups rely on a fraud-proving mechanism: there is a challenge period during which anyone can submit a fraud proof if they detect an invalid transaction. If a fraud proof is successful, the rollup state is corrected and the malicious operator penalized. If no fraud proof is submitted, the state is accepted as valid. See [Optimistic Rollups](https://ethereum.org/en/developers/docs/scaling/optimistic-rollups/) for more details.

Prominent implementations: [[Optimism]], [[Arbitrum]]

### ZK Rollup

ZK Rollups use cryptographic validity proofs (e.g., zk-SNARKs) to prove that off-chain transactions are correct. The rollup operator generates a succinct proof for each batch and submits it to Ethereum, where a smart contract verifies the proof and updates the rollup state. ZK rollups do not require a challenge period, as invalid batches cannot be posted. However, generating proofs is computationally intensive, and EVM compatibility is more limited (though zkEVMs are advancing rapidly). See [ZK Rollups](https://ethereum.org/en/developers/docs/scaling/zk-rollups/) for more details.

Prominent implementations: [[ZKSync]], [[Linea]], Polygon zkEVM (see [[Polygon]])

## Optimistic Rollup vs ZK Rollup

|        Criteria        | Optimistic Rollup                                                                                          | ZK Rollup                                                                                              |
| :--------------------: | ---------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
|         Costs          | Major cost comes from submitting batches to Ethereum                                                       | Major cost comes from generating zk proofs                                                             |
| Ethereum Compatibility | Highest smart contract compatibility with Ethereum; supports most contracts without modification           | Lower smart contract compatibility; requires developers to adapt or rewrite contracts for zkEVMs       |
|        Security        | Relies on chain monitoring within the challenge window                                                     | No monitoring required, but relies on a trusted setup assumption (for some zk systems)                 |
|        Latency         | Lower latency for transaction confirmation, but higher latency for finality due to the challenge mechanism | Higher latency for transaction confirmation due to zk proof generation, but lower latency for finality |

## Recent Developments: Dencun Upgrade (EIP-4844)

The [[Dencun Upgrade (EIP-4844)]] (March 2024) introduced **Proto-Danksharding** and "blobspace" to Ethereum. This allows rollups to post large amounts of data (blobs) to Ethereum at much lower cost than traditional calldata. Blobs are stored temporarily (not indefinitely on-chain), which is sufficient for rollup data availability and drastically reduces fees for rollup users. This upgrade is a major milestone for Ethereum scalability, making rollups more affordable and paving the way for full Danksharding in the future.

## Major Rollup Implementations

- [[Optimism]]: An optimistic rollup with high EVM compatibility, powering the OP Mainnet and the broader Superchain ecosystem.
- [[Arbitrum]]: Another leading optimistic rollup, known for its high throughput and developer ecosystem.
- [[ZKSync]]: A zk-rollup focused on EVM compatibility and fast, low-cost transactions.
- [[Linea]]: A zkEVM rollup developed by ConsenSys, offering high EVM equivalence and developer-friendly tooling.
- [[Polygon]]: Offers both optimistic and zkEVM rollup solutions, including Polygon zkEVM.

## Related Concepts

- [[Ethereum]]
- [[Smart Contract]]
- [[Gas]]
- [[Optimism]]
- [[Arbitrum]]
- [[ZKSync]]
- [[Linea]]
- [[Polygon]]
- [[Dencun Upgrade (EIP-4844)]]

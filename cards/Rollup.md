#explain-card

## What is Rollup?  

Rollup is a scaling solution for Ethereum that bundles or "rolls up" multiple transactions into a single transaction on the Ethereum mainnet. These rollup transactions are executed on an off-chain rollup network. To inherit Ethereum's security, the rollup network regularly submits transaction data to the Ethereum mainnet. Once the data is uploaded and stored on Ethereum, reverting a rollup transaction requires reverting the Ethereum transaction. This mechanism allows the single transaction fee on Ethereum to be distributed among many transactions in the rollup network, reducing the overall transaction cost.

## Types of Rollup

There are two main popular  types of rollup solution: Optimistic rollup and ZK rollup. They differ in how they handle transaction verification and data availability.

### Optimistic rollup

Optimistic rollup assumes that transactions are valid by default, the rollup transactions are executed once received and the execution result will be available in the rollup network. Then the rollup operator will bunch these transactions data regularly and submit them to the Ethereum mainnet as calldata or blobs.  Optimistic rollup relies on a fraud-proving mechanism to detect the cases that transactions are not executed correctly. There is a time window called challenge period for users to submit fraud proofs to challenge the incorrect rollup transactions. 

### ZK rollup

### Optimistic rollup vs ZK rollup


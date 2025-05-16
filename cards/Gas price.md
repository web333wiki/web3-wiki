#explain-card 

## Introduction

This card explains the concept of gas prices within the [[Ethereum]] network. Gas prices are integral to how [[Ethereum]] functions, representing the cost of performing operations on the blockchain. Understanding gas prices is crucial for users and developers interacting with [[Ethereum]] to manage transaction costs effectively.

## Key Concepts

- **[[Gas]]**: The computational effort required to execute specific operations on the [[Ethereum]] network. Every operation, from a simple transfer to a complex smart contract interaction, has a fixed amount of gas associated with it.
- **Gas Price**: The amount of [[Ethereum]] a user is willing to pay per unit of gas. Gas prices are typically denoted in Gwei, which is a smaller denomination of [[Ethereum]] (1 Gwei = 0.000000001 [[Ethereum]]).
- **Transaction Fee**: The total cost a user pays for a transaction. It is calculated as: `Gas Used * Gas Price`.
- **[[Gas limit]]**: The maximum amount of gas a user is willing to spend on a transaction. This prevents situations where a faulty smart contract consumes an excessive amount of gas.
- **Gwei**: A denomination of Ether, commonly used for specifying gas prices. 1 Ether = 1,000,000,000 Gwei.

## How Gas Prices Work

When a user initiates a transaction on the [[Ethereum]] network, they must specify a gas price they are willing to pay. Validators (previously miners before [[The Merge]]) prioritize transactions with higher gas prices because they receive the transaction fees as a reward for including the transaction in a block.

Think of it as a bidding system: users bid with gas prices to get their transactions processed. If the network is congested, users need to offer higher gas prices to incentivize validators to include their transactions sooner. Conversely, when network activity is low, gas prices tend to be lower.

[[Ethereum]] wallets and applications often suggest gas prices based on current network conditions. Users can typically choose between slow, average, or fast transaction speeds, which correspond to lower, medium, or higher gas prices, respectively. Setting a gas price too low might result in the transaction being delayed significantly or even getting stuck if validators do not find it profitable enough to include.

Since the implementation of EIP-1559, the transaction fee mechanism has two components:

1.  **Base Fee**: This is a protocol-defined fee per unit of gas that is burned (destroyed), not paid to validators. The base fee adjusts up or down based on network congestion, aiming to keep blocks about 50% full. If blocks are more than 50% full, the base fee increases; if less, it decreases.
2.  **Priority Fee (Tip)**: This is an additional fee set by the user that goes directly to the validator. It incentivizes validators to include a user's transaction over others, especially during times of high network congestion.

So, the total gas fee per unit of gas is `Base Fee + Priority Fee`. The total transaction cost is `(Base Fee + Priority Fee) * Gas Used`.

## Factors Influencing Gas Prices

Several factors contribute to the fluctuation of gas prices on the [[Ethereum]] network:

- **Network Congestion**: This is the primary driver. When many users are trying to get their transactions processed simultaneously (e.g., during popular [[NFT]] mints or [[Decentralized finance]] events), the demand for block space increases, leading to higher base fees and users offering higher priority fees to get their transactions included.
- **Transaction Complexity**: More complex transactions, such as interacting with sophisticated smart contracts, require more computational work and thus consume more gas. While this doesn't directly change the gas _price_ (Gwei per gas), it increases the overall transaction fee (Total Gas Used \* Gas Price).
- **Block Size Target**: EIP-1559 aims for an average block size. If blocks are consistently fuller than the target, the base fee automatically increases. If they are less full, the base fee decreases.
- **Market Demand for [[Ethereum]]**: The underlying value of [[Ethereum]] can indirectly influence perceived gas costs, as fees are paid in [[Ethereum]].
- **Data Storage and Computation**: Operations that store data on the blockchain or perform complex computations are more gas-intensive.

Users can monitor current gas prices using tools like [[Etherscan]]'s Gas Tracker to make informed decisions about when to transact and what gas price to set.

## See Also

- [[Ethereum]]
- [[Etherscan]]
- [[Gas]]
- [[Gas limit]]
- [[Gwei]]
- [[The Merge]]
- [[Smart contract]]
- [[NFT]]
- [[Decentralized finance]]

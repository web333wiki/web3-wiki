#explain-card 

The Nakamoto Coefficient is a fundamental metric for evaluating the decentralization of blockchain networks. Named after Bitcoin's pseudonymous creator Satoshi Nakamoto, this metric represents the minimum number of entities that would need to collude to disrupt the network's operations.

A higher Nakamoto Coefficient indicates greater decentralization and network resilience. For example, a coefficient of 7 means at least 7 different entities would need to cooperate to potentially censor transactions or execute a 51% attack. This metric is particularly important for assessing:

- Proof of Stake networks (by validator stake distribution)
- Proof of Work networks (by mining pool distribution)
- Governance systems (by voting power distribution)

To calculate the Nakamoto Coefficient:
1. Identify the critical subsystem being measured (mining, validation, governance)
2. Determine the minimum threshold of control needed (typically 33% or 51%)
3. Rank all participants by their share of power/stake
4. Cumulatively add the largest participants until reaching the threshold
5. The number of participants at this point is the Nakamoto Coefficient

You can explore real-time Nakamoto Coefficient data for various blockchains at [NakaFlow.io](https://nakaflow.io/), which provides up-to-date metrics for supported chains.
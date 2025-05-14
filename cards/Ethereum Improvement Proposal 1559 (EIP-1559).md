#explain-card

## Overview

**Ethereum Improvement Proposal 1559 (EIP-1559)** is a major upgrade to Ethereum's transaction fee mechanism, implemented as part of the [[London Hard Fork]] in August 2021. It fundamentally changed how gas fees are calculated and handled, aiming to improve user experience by making fees more predictable and introducing a deflationary aspect to ETH through fee burning.

- **Problem Solved:** Addressed issues with the previous first-price auction fee model, which led to volatile and unpredictable gas prices, overpayment, and a poor user experience. It also aimed to better align ETH's monetary policy with network usage.
- **Value Proposition:** Introduced a base fee that adjusts algorithmically based on network congestion, a priority fee (tip) for miners/validators, and the burning of the base fee, making ETH potentially deflationary.
- **Status:** Live on Ethereum since the London Hard Fork (August 5, 2021).

## Key Mechanisms

EIP-1559 introduced a new fee structure consisting of two main components:

1.  **Base Fee (`baseFeePerGas`):**

    - This is a mandatory fee for including a transaction in a block.
    - It is determined algorithmically by the protocol based on network congestion. If blocks are more than 50% full (the target gas limit per block is 15 million, but blocks can expand up to 30 million gas), the base fee increases. If blocks are less than 50% full, the base fee decreases.
    - The base fee is **burned** (destroyed), meaning it is removed from circulation. This acts as a deflationary pressure on ETH supply, as more ETH is burned when network activity is high.

2.  \*\*Priority Fee (`maxPriorityFeePerGas` or Tip):
    - This is an optional fee paid directly to miners (pre-Merge) or validators (post-Merge) to incentivize them to include a transaction in a block.
    - Users can set a tip to prioritize their transactions, especially during times of high congestion.

Additionally, users specify a **Max Fee (`maxFeePerGas`):**
_ This is the absolute maximum amount a user is willing to pay per unit of gas for their transaction, including both the base fee and the priority fee.
_ If the `baseFeePerGas` plus the `maxPriorityFeePerGas` exceeds the `maxFeePerGas`, the transaction will wait until the base fee drops or the user increases their max fee. \* Users are refunded the difference between `maxFeePerGas` and (`baseFeePerGas` + `maxPriorityFeePerGas`).

## Impact and Benefits

- **Fee Predictability:** While not fixing gas prices, EIP-1559 makes them more predictable by having the base fee adjust smoothly based on demand, rather than relying purely on a blind auction.
- **Reduced Overpayment:** Users can set a `maxFeePerGas` they are comfortable with, knowing they won't pay more than the prevailing base fee plus their chosen tip.
- **ETH Burning (Deflationary Pressure):** The burning of the base fee directly links network usage to a reduction in ETH supply. During periods of high network demand, more ETH can be burned than is issued through block rewards (especially post-Merge), potentially making ETH a deflationary asset.
- **Improved User Experience:** Wallets can more easily estimate appropriate fees.

## Considerations

- **Doesn't Lower Gas Fees Directly:** EIP-1559 is not primarily designed to lower gas fees, but rather to make them more predictable and efficient. High demand will still lead to high base fees.
- **Elastic Block Sizes:** Blocks can temporarily expand up to twice the target gas limit to absorb demand spikes, helping to smooth out fee volatility.

## Related Concepts

- [[Ethereum]]
- [[Gas]]
- [[London Hard Fork]]
- [[Transaction Fees]]
- [[ETH (Ether)]]

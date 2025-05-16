#explain-card

## Overview

The **Pectra Upgrade** is the next major planned hard fork for the Ethereum network, anticipated to follow the [[Dencun upgrade]]. It combines two simultaneous upgrades: "Prague" for the execution layer and "Electra" for the consensus layer. Pectra is expected to be a feature-rich upgrade, focusing on several key areas including improvements to staking, enhancements to account abstraction (building on EIP-7702), and further support for Layer 2 scaling.

- **Problem Solved:** Aims to address various aspects of Ethereum's functionality, including validator user experience, core account features, and network efficiency, particularly concerning staking and Layer 2 data availability.
- **Value Proposition:** Expected to deliver a more user-friendly staking experience, more powerful and flexible account capabilities, and continued improvements to Ethereum's scalability and efficiency as a global settlement layer.
- **Status:** In development, with EIPs under discussion and testing. The mainnet activation date is tentatively scheduled for late 2024 or early 2025 (specific dates are subject to change based on development and testing progress).

## Key Expected Features and EIPs (Subject to Change)

The Pectra upgrade is likely to include a bundle of Ethereum Improvement Proposals. While the final list can evolve, some of the prominent EIPs being considered are:

1.  **EIP-7702: Set EOA account code (Account Abstraction)**

    - Allows Externally Owned Accounts (EOAs) to temporarily act like smart contract accounts for the duration of a transaction. This enables features like transaction batching, gas sponsorship, and alternative authentication methods (e.g., passkeys) without requiring users to migrate to full smart contract accounts.

2.  **EIP-7251: Increase `MAX_EFFECTIVE_BALANCE`**

    - Raises the maximum effective balance for a validator from 32 ETH to 2048 ETH. This allows large stakers to consolidate their stake into fewer validators, reducing the total number of validators on the network and potentially improving network efficiency and performance. It also enables rewards to compound beyond 32 ETH for individual validators.

3.  **EIP-7002: Execution layer triggerable exits**

    - Allows validator exits to be initiated from the execution layer (e.g., by a smart contract or an EOA with withdrawal credentials), providing more flexibility and automation for staking operations and services.

4.  **EIP-6110: Supply validator deposits on-chain**

    - Streamlines the validator deposit process by moving it to the execution layer, making it more transparent and predictable.

5.  **EIP-7691: Blob throughput increase (Further L2 Scaling Support)**

    - Expected to further increase the number of data blobs that can be included per block (e.g., doubling the target from 3 to 6 and the max from 6 to 9), building on the blobspace introduced in the [[Dencun upgrade]] to further reduce costs for Layer 2 rollups.

6.  **EIP-2537: Precompile for BLS12-381 curve operations**

    - Adds a precompile for efficient BLS signature verification, which is beneficial for staking, cross-chain bridges, and other advanced cryptographic applications.

7.  **Other potential EIPs:** May include improvements to EVM functionality, state management (like Verkle Tree preparations), and network performance.

## Expected Impact

- **Enhanced Staking UX:** Making staking more accessible, efficient, and flexible for both individual stakers and large institutions.
- **Improved Wallet Functionality:** Bringing smart account features to standard EOAs, significantly upgrading user experience for everyday transactions.
- **Lower L2 Fees:** Continued reduction in data availability costs for Layer 2 solutions, further boosting scalability.
- **Network Efficiency:** Optimizations related to validator counts and data handling.

## Related Concepts

- [[Ethereum]]
- [[Proof of stake]]
- [[Validator]]
- [[Staking]]
- Layer 2 Rollups (or [[Rollup]])
- [[Dencun upgrade]]

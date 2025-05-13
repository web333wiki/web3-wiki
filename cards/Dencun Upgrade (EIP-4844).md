#explain-card

## Overview

The **Dencun Upgrade** (also known as Cancun-Deneb) is a significant Ethereum network upgrade that went live on March 13, 2024. Its most notable feature is the introduction of **Proto-Danksharding** through **Ethereum Improvement Proposal 4844 (EIP-4844)**. This EIP aims to drastically reduce transaction fees for Layer 2 rollups and improve Ethereum's overall scalability by introducing a new way for rollups to post data to the Ethereum mainnet.

- **Problem Solved:** High data posting costs for Layer 2 rollups on Ethereum Layer 1. Rollups previously used `CALLDATA` to submit transaction data, which is expensive as it's processed by all Ethereum nodes and stored on-chain indefinitely. EIP-4844 provides a cheaper, more efficient alternative.
- **Value Proposition:** Significantly lowers Layer 2 transaction costs, making dApps on rollups more affordable and enhancing Ethereum's competitiveness as a scalable blockchain.
- **Status:** Live on Ethereum since March 13, 2024.

## Key Mechanisms of EIP-4844 (Proto-Danksharding)

EIP-4844 introduces several key components:

1.  \*\*Blob-Carrying Transactions (Blobs):

    - A new transaction type that allows Layer 2 rollups to post large amounts of data (up to ~128 KB per blob, with a target of 3 blobs and a max of 6 blobs per block initially) to Ethereum in a dedicated, temporary storage space called "blobspace."
    - Blobs are separate from `CALLDATA` and are not accessed by the EVM (Ethereum Virtual Machine).
    - Data in blobs is only guaranteed to be available for a limited period (e.g., ~18 days, pruned by consensus layer clients), which is sufficient for rollups to retrieve and verify it, but avoids long-term storage costs on Layer 1.

2.  **New Fee Market for Blobs:**

    - Blobspace has its own fee market, separate from the regular gas market for `CALLDATA` and EVM execution. This means the cost of posting blobs is independent of Ethereum's mainnet gas prices.
    - Fees for blobs are expected to be significantly lower than using `CALLDATA`.

3.  \*\*KZG Commitments (Kate-Zaverucha-Goldberg Commitments):
    - Cryptographic commitments used to verify the availability of blob data without requiring nodes to download entire blobs. This is a step towards full Danksharding, where data availability sampling (DAS) will allow nodes to verify large amounts of data with minimal overhead.

## Impact and Benefits

- **Reduced Layer 2 Fees:** The primary benefit is a substantial reduction in the cost for users transacting on Layer 2 rollups, as the data fees paid by rollups to Ethereum L1 decrease significantly.
- **Improved Ethereum Scalability:** By making rollups cheaper and more efficient, Dencun helps Ethereum scale its transaction throughput capacity.
- **Path to Full Danksharding:** Proto-Danksharding implements many of the transaction formats, cryptographic schemes (KZG commitments), and logic that will be used in full Danksharding, which promises even greater scalability.
- **Enhanced Data Availability:** While temporary, blobs provide a dedicated and cost-effective channel for data availability for rollups.

## Other EIPs in Dencun

Besides EIP-4844, the Dencun upgrade included other EIPs focused on various improvements, such as EVM enhancements and minor adjustments to gas costs for specific operations. Key ones include:

- EIP-1153: Transient storage opcodes
- EIP-4788: Beacon block root in the EVM
- EIP-5656: MCOPY - Memory copying instruction
- EIP-6780: SELFDESTRUCT only in same transaction

## Related Concepts

- [[Ethereum]]
- [[Layer 2 Rollups]] (or [[Rollup]])
- [[Transaction Fees]]
- [[Gas]]
- [[Scalability]]
- [[Data Availability]]
- [[The Merge]] (as a precursor to further scaling upgrades)

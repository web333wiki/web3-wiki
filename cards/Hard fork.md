#explain-card

## Introduction & Definition

A **hard fork** is a radical change to a blockchain's protocol that makes previously invalid blocks/transactions valid, or vice-versa. It requires all nodes or users to upgrade to the latest version of the protocol software. A hard fork is a permanent divergence from the previous version of the blockchain, and nodes running the old version will not be accepted by the newest version. Think of it as a software upgrade that is not backward-compatible.

Essentially, a hard fork is a rule change such that the software validating blocks according to the old rules will see blocks produced according to the new rules as invalid. Conversely, software validating blocks according to the new rules will see blocks produced according to the old rules as invalid.

**Analogy (ELI5):** Imagine a popular board game that everyone in a club plays by a certain set of rules (the old blockchain protocol). One day, a proposal is made to significantly change some core rules (the hard fork).

- If almost everyone agrees and adopts the new rules, the game continues with the new rulebook.
- If a significant portion of the club members decide they prefer the old rules, they might split off and continue playing with the old rulebook, while the others play with the new one. Now, there are two separate versions of the game being played by two different groups, and their game states (scores, progress) are no longer compatible.

**Importance & Purpose:**
Hard forks are crucial mechanisms for blockchains to:

- **Upgrade the network:** Implement significant improvements, new features, or technological advancements.
- **Fix critical security vulnerabilities:** Address urgent security issues that cannot be fixed with a less disruptive [[Soft fork]].
- **Resolve community disagreements:** Sometimes, a hard fork is the result of a fundamental disagreement within the community about the future direction of the project.
- **Reverse transactions:** In controversial cases, a hard fork can be used to reverse certain transactions or effects, as seen with the DAO hack.

## Core Principles & Detailed Mechanism

When a hard fork occurs, the blockchain splits into two: one chain follows the new set of rules, and the other continues with the old rules (if there are still nodes and miners/validators supporting it).

- **Rule Changes:** The new rules implemented in a hard fork are incompatible with the old rules. For example, a hard fork might change the block size, the consensus algorithm, or how transaction fees are calculated.
- **Node Upgrades:** All participants (nodes, miners/validators) who wish to remain on the updated network must upgrade their software to comply with the new rules. Those who don't upgrade will be left on the old chain, which will operate as a separate blockchain.
- **Chain Split:** If there's significant support for both the old and new rules, the hard fork can lead to a permanent chain split, resulting in two separate blockchains and potentially two separate cryptocurrencies. The original cryptocurrency continues on one fork, and a new cryptocurrency is created on the other.

**Types of Hard Forks:**

- **Non-Contentious (Planned) Hard Forks:** These are typically scheduled upgrades agreed upon by the vast majority of the community. The goal is to improve the network, and there's little intention to maintain the old chain. Most nodes upgrade, and the old chain quickly becomes obsolete.
- **Contentious Hard Forks:** These occur when there's a significant disagreement within the community about the proposed changes. This often leads to a persistent chain split, with both chains co-existing and being supported by different factions of the community. This can lead to the creation of a new cryptocurrency (e.g., Bitcoin Cash from Bitcoin, Ethereum Classic from Ethereum).

## Practical Applications, Use Cases & Implications

**Examples of Hard Forks:**

- **The DAO Hard Fork (2016):** This occurred on the [[Ethereum]] network to reverse the effects of [The DAO Hack](https://cryptodose.net/learn/the-dao-hack/), where a large amount of Ether was stolen from a decentralized venture fund. The majority of the Ethereum community agreed to the hard fork to recover the funds. However, a minority disagreed with altering the blockchain's history, leading to a split. The original, unaltered chain continued as Ethereum Classic (ETC), while the forked chain retained the name Ethereum (ETH).
- **Bitcoin Cash (2017):** A hard fork from [[Bitcoin]] primarily due to disagreements over how to scale the network. Bitcoin Cash increased the block size limit to allow for more transactions per block.
- **Ethereum's Upgrades:** Many of Ethereum's major upgrades, like "The Merge" (transition to Proof-of-Stake), were implemented via hard forks, but these were largely planned and non-contentious, with overwhelming community support.

**Benefits & Advantages:**

- Allows for significant protocol upgrades and innovation.
- Can resolve fundamental issues or vulnerabilities.
- Offers a way for communities to pursue different development paths if disagreements arise.

**Limitations, Challenges & Criticisms:**

- **Community Splits:** Contentious hard forks can divide the community and developer base.
- **New Cryptocurrency Creation:** While sometimes intended, the creation of a new coin can cause confusion and dilute market value.
- **Replay Attacks:** If not properly managed (e.g., with replay protection), transactions on one forked chain could be "replayed" on the other, potentially leading to loss of funds.
- **Exchange and Wallet Support:** Services need to decide which fork(s) to support, which can be disruptive for users.
- **Security of Minority Chains:** A chain resulting from a contentious hard fork with significantly less hashing power (in Proof of Work systems) can be more vulnerable to attacks.
- **Philosophical Concerns:** Some argue that hard forks, especially those that alter transaction history, undermine the principle of immutability.

## Related Concepts

- [[Soft fork]]
- [[Consensus]]
- [[Block]]
- [[Node]]
- [[Ethereum]]
- [[Bitcoin]]

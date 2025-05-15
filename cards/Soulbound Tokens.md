#explain-card

## Introduction

**Soulbound Tokens (SBTs)** are a concept for non-transferable, publicly verifiable digital tokens that represent aspects of a person's or entity's identity, commitments, credentials, affiliations, or reputation within a blockchain ecosystem. Proposed by E. Glen Weyl, Puja Ohlhaver, and Vitalik Buterin in May 2022, SBTs are envisioned as a way to create a richer, more trustworthy social identity layer for Web3, often referred to as a "Decentralized Society" (DeSoc).

- **Importance/Purpose:** SBTs aim to address limitations of the current Web3 identity landscape, which is often characterized by anonymity or easily transferable/tradable identifiers (like ENS names or NFTs representing identity). By being non-transferable, SBTs are intended to represent qualities or achievements that are intrinsically tied to an individual or entity and cannot (or should not) be bought or sold.
- **Target Audience:** Web3 users, developers building identity and reputation systems, DAOs, and communities looking for new ways to manage membership, roles, and attestations.

## Core Concepts & Mechanism

### Key Characteristics

1.  **Non-Transferable:** This is the defining feature. Once an SBT is issued to a specific blockchain account (a "Soul"), it cannot be transferred or sold to another account. This ensures that the attribute or reputation represented by the SBT remains tied to the original recipient.
2.  **Publicly Verifiable:** Like other blockchain tokens, the issuance and ownership of SBTs can be publicly verified on the blockchain.
3.  **Issued by Souls to Souls:** SBTs are issued by one Soul (e.g., an institution, a DAO, another individual) to another Soul. For example, a university (Soul) could issue an SBT representing a degree to a graduate (Soul).
4.  **Potential for Revocation:** Issuers might have the ability to revoke SBTs they have issued (e.g., if a credential is no longer valid).
5.  **Community Recovery:** A proposed mechanism for Souls to recover access if they lose their private keys, potentially involving a qualified majority of a Soul's established "community" of relationships (other Souls who have issued SBTs to them or received SBTs from them).

### How SBTs Might Work

- **Souls:** A Soul is essentially a blockchain account or wallet that holds SBTs.
- **Issuance:** An entity (e.g., a university, an employer, a conference organizer, a DAO) issues an SBT to a user's Soul. This SBT could represent a degree, employment history, attendance record, membership status, or a skill attestation.
- **Attestation & Reputation:** Over time, a Soul would accumulate various SBTs from different issuers, forming a rich, verifiable on-chain profile of their affiliations, credentials, and experiences.
- **Use in dApps:** Decentralized applications could then use these SBTs to grant access, determine roles, calculate reputation scores, or enable new forms of governance (e.g., voting based on proven expertise or contribution).

## Use Cases & Implications

### Potential Applications

- **Identity & Reputation:** Creating more robust and trustworthy online identities.
- **Credentials & Achievements:** Representing educational degrees, professional certifications, skills, and attendance records.
- **Community Membership & Governance:** Managing DAO membership, voting rights, and roles based on contributions or attestations.
- **Proof of Personhood:** Contributing to solutions for Sybil resistance (preventing one person from creating many fake accounts).
- **Uncollateralized Lending:** Potentially enabling undercollateralized loans based on social reputation represented by SBTs, rather than just crypto collateral.
- **Event Ticketing & POAPs:** Non-transferable proof of attendance or participation.
- **Combating Misinformation:** SBTs from trusted attestors could help verify the provenance or authenticity of content or claims.

### Benefits

- **Richer Social Identity:** Moves beyond purely financial or anonymous interactions in Web3.
- **Increased Trust:** Allows for the creation of verifiable reputation systems.
- **Sybil Resistance:** Helps in distinguishing unique individuals from bots or multiple accounts controlled by a single entity.
- **New Forms of Governance:** Enables more nuanced and meritocratic governance models in DAOs.

### Limitations & Challenges

- **Privacy Concerns:** While SBTs are non-transferable, their public verifiability means that a Soul's affiliations and credentials could be easily tracked. Mechanisms for selective disclosure or privacy-preserving SBTs are important considerations.
- **Social Control/Dystopian Risks:** Critics worry that SBTs could lead to systems of social credit or exclusion if not designed carefully.
- **Irreversibility & Harassment:** A negatively connotated SBT, once issued, might be hard to get rid of if revocation mechanisms aren't robust or fair. Malicious issuance of SBTs could be a form of harassment.
- **Key Management & Recovery:** The concept of community recovery for lost keys is novel but complex to implement securely and fairly.
- **Bootstrapping Problem:** The value of SBTs depends on a network effect – they become useful once many issuers and verifiers adopt them.
- **Defining "Soul":** Ensuring a Soul corresponds to a unique individual or entity and preventing gaming of the system remains a challenge.

## Related Concepts

- [[Decentralized Identity (DID)]]
- non-fungible token (NFT) (SBTs are often conceptualized as non-transferable NFTs)
- decentralized autonomous organization (DAO)
- proof of personhood
- reputation systems
- verifiable credentials
- privacy
- [[Web3]]

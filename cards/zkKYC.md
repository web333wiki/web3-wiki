#explain-card

## Introduction

**zkKYC (Zero-Knowledge Know Your Customer)** refers to emerging systems and protocols that aim to fulfill [[Know Your Customer (KYC)|Know Your Customer]] (KYC) requirements using [[Zero-Knowledge Proof (ZKP)|Zero-knowledge proof]]s (ZKPs). The core idea is to allow users to prove to a verifier (e.g., a financial service) that they meet certain regulatory criteria (e.g., are not on a sanctions list, are over 18, are from a specific jurisdiction) without revealing their actual personal identifiable information (PII).

- **Importance/Purpose:** zkKYC seeks to balance the need for regulatory compliance in Web3 with the strong desire for user privacy and data minimization. It offers a potential solution to the privacy concerns associated with traditional KYC, where users must hand over sensitive data to service providers.
- **Target Audience:** Users concerned about privacy, Web3 platforms needing to comply with regulations, identity solution developers, and regulators exploring privacy-preserving technologies.

## Core Concepts & Mechanism

### Key Components

1.  **User:** The individual who needs to prove certain attributes about themselves.
2.  **Identity Provider (IdP) / Attester:** A trusted entity (e.g., a government agency, a specialized KYC service, a bank) that has already verified the user's identity through traditional means and can issue cryptographic attestations or credentials about the user (e.g., "User X is a resident of Country Y").
3.  **Verifier / Service Provider:** The entity that needs to check if the user meets certain KYC criteria (e.g., a [[Decentralized Finance (DeFi)]] protocol, an exchange).
4.  **Zero-Knowledge Proof System:** The underlying cryptographic technology (e.g., [[Zero-Knowledge Succinct Non-Interactive Argument of Knowledge (zk-SNARKs)|zk-SNARKs]], zk-STARKs) that allows the user to generate a proof of an assertion without revealing the underlying data.

### How zkKYC Works (Generalized Flow)

1.  **Traditional KYC with IdP:** The user first completes a standard KYC process with a trusted Identity Provider.
2.  **Issuance of Attestation/Credential:** The IdP issues a digitally signed attestation or credential to the user. This credential cryptographically binds certain attributes to the user's wallet or a decentralized identifier ([[Decentralized Identity (DID)]]). For example, it might attest that the wallet holder is not on a specific watchlist.
3.  **Proof Generation:** When the user wants to access a service requiring KYC, their software generates a zero-knowledge proof. This proof demonstrates that they hold a valid credential from a recognized IdP satisfying the service's requirements (e.g., "I possess an attestation from IdP Z showing I am not on Sanctions List A"). The proof itself does not reveal the user's name, date of birth, or other PII contained in the original credential.
4.  **Proof Verification:** The service provider verifies the ZKP. If the proof is valid, the user is granted access, having met the KYC requirement without disclosing their underlying data to the service provider.

### Variations and Approaches

- **On-Chain vs. Off-Chain Attestations:** Attestations can be stored on-chain (e.g., as non-transferable NFTs or [[Soulbound Tokens]]) or off-chain.
- **Different ZKP Schemes:** Various ZKP technologies can be used, each with different trade-offs in terms of proof size, proving time, and trusted setup requirements.
- **Selective Disclosure:** Some systems might allow for more granular selective disclosure, where a user can prove specific attributes (e.g., "I am over 18") from a broader set of attested information.

## Use Cases & Implications

### Benefits

- **Enhanced Privacy:** Users can meet regulatory requirements without exposing sensitive PII to every service they interact with, reducing the risk of data breaches and surveillance.
- **Reduced Data Silos:** Lessens the need for multiple service providers to collect and store the same KYC data repeatedly.
- **Improved User Experience:** Potentially streamlines onboarding by allowing users to reuse attestations across different services.
- **Regulatory Compliance:** Offers a pathway for Web3 services to comply with KYC/AML regulations in a more privacy-respecting manner.

### Limitations & Challenges

- **Complexity:** ZKP technology is complex to implement and audit.
- **Trust in Identity Providers:** zkKYC still relies on trusted IdPs to perform the initial identity verification correctly and issue trustworthy attestations. The decentralization of this trust is a challenge.
- **Revocation:** Securely and privately revoking attestations (e.g., if a user's status changes) is a complex problem.
- **Scalability and Cost:** Generating and verifying ZKPs can be computationally intensive and may incur costs.
- **Adoption and Standardization:** Widespread adoption requires standardization of protocols and acceptance by regulators.
- **Oracle Problem for Attributes:** Ensuring the attributes attested by IdPs are accurate and up-to-date can be challenging (e.g., an IdP attesting someone is _not_ on a sanctions list needs real-time, accurate sanction list data).

## Related Concepts

- [[Zero-Knowledge Proof (ZKP)]]
- [[Know Your Customer (KYC)]]
- [[Anti-Money Laundering (AML)]]
- [[Decentralized Identity (DID)]]
- [[Soulbound Tokens]] (as a potential way to represent attestations)
- Privacy
- [[Data Security]]
- [[Regulation]]

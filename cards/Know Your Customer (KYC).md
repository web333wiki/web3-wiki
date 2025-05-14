#explain-card

## Introduction

**Know Your Customer (KYC)** refers to the mandatory process of identifying and verifying the identity of clients, typically by financial institutions, but increasingly by other regulated entities and services, including many within the Web3 ecosystem. The primary purpose of KYC is to prevent illicit activities such as money laundering, terrorist financing, and fraud by ensuring that businesses know who their customers are. This process usually involves collecting personal identification information (PII) like government-issued IDs (passports, driver's licenses), proof of address (utility bills, bank statements), and sometimes biometric data.

- **Importance/Purpose:** In traditional finance (TradFi), KYC is a cornerstone of regulatory compliance (e.g., Anti-Money Laundering (AML) and Counter-Terrorist Financing (CTF) laws). In Web3, its application is more debated and varied. While some platforms, especially centralized exchanges (CEXs) and services interacting with fiat currencies, implement KYC to comply with regulations, many decentralized finance (DeFi) protocols and privacy-focused projects aim to minimize or avoid KYC to preserve user anonymity and reduce censorship risk. The tension between regulatory compliance and the pseudonymous nature of many blockchains makes KYC a significant topic in Web3.
- **Target Audience:** Users of financial services (both traditional and crypto-related), Web3 developers, investors, and policymakers.

## Core Concepts & Mechanism

### Key Components of KYC

1.  **Customer Identification Program (CIP):** The foundational part, requiring the collection of identifying information from customers. This usually includes name, date of birth, address, and identification number (e.g., social security number or national ID).
2.  **Customer Due Diligence (CDD):** Involves verifying the collected information and assessing the risk associated with a customer. This can range from simple verification against databases to more enhanced due diligence (EDD) for higher-risk individuals (e.g., Politically Exposed Persons - PEPs).
3.  **Ongoing Monitoring:** Continuously monitoring customer transactions and account activity to detect suspicious patterns or changes in risk profile.

### How KYC Works (General Process)

1.  **Information Collection:** The user provides requested PII through an online form or application.
2.  **Document Submission:** The user uploads copies of identification documents (e.g., passport, ID card, proof of address).
3.  **Verification:** The service provider (or a third-party KYC provider) verifies the authenticity of the documents and the identity of the user. This may involve:
    - Checking documents against government databases.
    - Using liveness detection and facial recognition to match the user with their ID photo.
    - Cross-referencing information with credit bureaus or other data providers.
4.  **Risk Assessment:** The user is assigned a risk score based on factors like location, transaction patterns, and watchlists (e.g., for sanctions or PEPs).
5.  **Approval/Rejection:** Based on the verification and risk assessment, the user's account is approved, or further information is requested. In some cases, access may be denied.

### KYC in Web3

The implementation of KYC in the Web3 space varies significantly:

- **Centralized Exchanges (CEXs):** Most CEXs (e.g., [[Coinbase]], [[Binance]]) require KYC for users to deposit, withdraw, or trade significant amounts, especially when fiat currency on/off ramps are involved. This is to comply with regulations in the jurisdictions they operate in.
- **Decentralized Exchanges (DEXs) & DeFi:** Many DEXs and DeFi protocols aim to be permissionless and do not require KYC for basic swapping or liquidity provision directly on-chain. However, access to their front-ends or participation in certain governance aspects might sometimes involve forms of identity verification, or KYC might be required by platforms that offer access to these DeFi protocols with added services.
- **NFT Marketplaces:** KYC requirements on NFT marketplaces are evolving. Some may require it for high-value transactions or specific collections.
- **Privacy-Preserving Solutions:** There's ongoing research and development into "Decentralized Identity" (DID) solutions and [[Zero-Knowledge Proof (ZKP)]] (ZKPs) that could potentially allow users to prove certain attributes (e.g., not being on a sanctions list, being over 18) without revealing their full identity. This could offer a path to regulatory compliance while preserving user privacy. An example is [[zkKYC]].

## Use Cases & Implications

### Benefits of KYC

- **Regulatory Compliance:** Helps businesses meet legal obligations and avoid penalties.
- **Prevention of Financial Crime:** Deters money laundering, terrorist financing, and fraud.
- **Enhanced Security:** Can help prevent unauthorized account access and identity theft (though PII data breaches are a counter-risk).
- **Increased Trust & Legitimacy:** Can make platforms appear more trustworthy to mainstream users and institutional investors.

### Limitations & Challenges of KYC

- **Privacy Concerns:** Involves the collection and storage of sensitive personal data, raising concerns about data breaches, surveillance, and misuse of information. The ethos of many Web3 projects prioritizes user privacy and anonymity.
- **Financial Exclusion:** Strict KYC requirements can be a barrier for individuals in developing countries who may lack official identification documents or a verifiable address. This contradicts the Web3 goal of financial inclusion.
- **Centralization Risk:** KYC data is often stored in centralized databases, creating single points of failure and attractive targets for hackers.
- **Cost & Friction:** Implementing KYC processes can be expensive for businesses and cumbersome for users, adding friction to onboarding.
- **Censorship Risk:** Governments or platforms could use KYC information to censor or restrict access to financial services for certain individuals or groups.
- **Effectiveness Debate:** Critics question the overall effectiveness of KYC/AML regimes in preventing financial crime, arguing that they are costly and invasive without delivering proportionate results.

### KYC and the Future of Web3

The role of KYC in Web3 is a subject of ongoing debate and innovation. Key trends include:

- **Regulatory Scrutiny:** Increasing pressure from regulators worldwide for Web3 platforms to implement KYC/AML measures.
- **Privacy-Enhancing Technologies:** Development of DIDs, ZKPs, and other cryptographic methods to enable compliance without compromising user privacy (e.g., [[Soulbound Tokens]] for attestations).
- **On-Chain KYC/Identity:** Exploring ways to represent KYC status or identity attributes directly on the blockchain in a secure and verifiable manner.

## Related Concepts

- [[Anti-Money Laundering (AML)]]
- [[Counter-Terrorist Financing (CTF)]]
- [[Centralized Exchange (CEX)]]
- [[Decentralized Finance (DeFi)]]
- [[Decentralized Identity (DID)]]
- [[Zero-Knowledge Proof (ZKP)]]
- [[Privacy Coins]]
- [[Regulation]]
- [[Financial Inclusion]]
- [[Data Security]]

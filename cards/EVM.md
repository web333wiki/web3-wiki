#explain-card

The Ethereum Virtual Machine (EVM) is the runtime environment for [[Smart contract|smart contracts]] in [[Ethereum]]. It is a decentralized, Turing-complete virtual machine that executes bytecode. Every [[Ethereum]] [[Node]] runs an instance of the EVM to maintain consensus across the blockchain.

## Purpose

The primary purpose of the EVM is to execute smart contracts and update the [[Ethereum]] state. It ensures that transactions are processed in a deterministic and trustless manner. The EVM enables developers to write decentralized applications (dApps) that run on the [[Ethereum]] network without a central authority.

Key functions include:

- **Smart Contract Execution**: Processes the logic within smart contracts.
- **State Management**: Maintains the global state of all accounts and contracts on [[Ethereum]].
- **Resource Management**: Utilizes a [[Gas]] system to measure computational effort and prevent abuse.

## Architecture

The EVM is a stack-based virtual machine. Its main components are:

- **Stack**: A LIFO (Last-In, First-Out) data structure where computations are performed. It has a maximum depth of 1024 items, and each item is a 256-bit word.
- **Memory**: A volatile, byte-addressable linear memory space used for temporary storage during contract execution. Memory is cleared after each message call.
- **Storage**: A persistent, word-addressable storage associated with each smart contract. Data stored here is part of the [[Ethereum]] global state and is permanently recorded on the blockchain.

## EVM Instructions (Opcodes)

The EVM executes smart contracts by processing a series of instructions called opcodes. These opcodes perform various operations, including:

- Arithmetic operations (e.g., ADD, SUB, MUL, DIV)
- Logical operations (e.g., AND, OR, XOR, NOT)
- Stack manipulation operations (e.g., PUSH, POP, DUP, SWAP)
- Memory and storage access (e.g., MLOAD, MSTORE, SLOAD, SSTORE)
- Control flow operations (e.g., JUMP, JUMPI)
- Blockchain-specific operations (e.g., ADDRESS, BALANCE, BLOCKHASH, [[Gas]])

Each opcode has an associated [[Gas]] cost, reflecting the computational resources required for its execution.

## Gas

[[Gas]] is the unit used to measure the computational work required to execute transactions or smart contracts on the EVM. Users pay gas fees in Ether (ETH) to incentivize miners/validators to process their transactions. The gas mechanism prevents network abuse and ensures fair resource allocation.

## Turing Completeness

The EVM is [[Turing complete]], meaning it can theoretically compute anything that any other [[Turing complete]] system can, given enough resources (like [[Gas]] and time). This allows for the creation of complex and sophisticated smart contracts.

## EVM Implementations

Various programming languages have implementations of the EVM, ensuring client diversity. Some notable implementations include:

- **Geth** (Go)
- **Nethermind** (.NET)
- **Besu** (Java)
- **Erigon** (Go, with components in other languages)
- **Py-EVM** (Python)
- **evmone** (C++)
- **ethereumjs-vm** (JavaScript)
- **revm** (Rust)

These implementations adhere to the EVM specification outlined in the [[Ethereum yellow paper]].

## Further Reading

- [Ethereum Virtual Machine (EVM) on Ethereum.org](mdc:https://ethereum.org/en/developers/docs/evm/)
- [[Ethereum yellow paper]]
- [[Solidity]] (The primary language for writing EVM-compatible smart contracts)

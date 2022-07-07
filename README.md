# Arcana Standard Contracts

This project contains ERC standard contracts with Arcana supported functions.


## Contracts

### ARC721: 

This ARC721 is a standard for representing ownership of non-fungible tokens, that is, where each token is unique. Which is compatible with ERC721 interface.

**Minting** : Use _mint_ function to create new tokens. function accepts receipent _Address_ and _token Id_ of newly minted token.

### Usage
Additional to ERC721 standard, we have to pass Bridge Address while deploying the contract.

#### _bridgeContractAddress_ for Mumbai
```
0x2a6137D49A5597aC3b26B7464Edf20A553291584
```
#### _bridgeContractAddress_ for Ropsten
```
0x491f0c066F6e126A34F57346613db5628B41ba18
```

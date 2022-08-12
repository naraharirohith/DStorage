# Arcana Smart Contracts

[![Build Status](https://www.travis-ci.com/arcana-network/smart-contract.svg?branch=main)](https://www.travis-ci.com/arcana-network/smart-contract)

Arcana's [Storage SDK](https://github.com/arcana-network/storage) features are powered and maintained by Arcana Smart Contracts.
- Handle's main file operations like upload, share, revoke, changeFileOwner, delete etc..
-  Storage SDK makes all its calls through meta-transactions which follow standard EIP Standards, EIP-2771 for making meta-transactions and EIP-1967 for making proxy calls.
- Handle's DIDs (Decentralized Identifiers) for files.
- Handle's private NFT data deployed on other chains.

## Contracts

### Logic Contract: Arcana.sol

This is the logic contract, input data will be passed through this contract but data will not be stored on this contract

### Proxy: ERC1967Proxy.sol

This will be the proxy contract. Users will call this contract. Calls will be delegated to the logic contract but all the data will be stored on this contract.

### Factory: Factory.sol

This contract is used to create multiple proxy contract. Each app will have it's own proxy contract but all of them will point to one logic contract.

### DID: DID.sol

This contract manages Decentralized Identifiers for the files.

### NFT Handler: NFTHandler.sol

This contract manages private NFT data which can be deployed on other chains.


## Pre Requisites
Copy .env.example to .env and set environment variables  
```
$ cp .env.example .env
```
Install dependencies
```sh
$ npm i
```

## Usage
### Compile

Compile the smart contracts with Hardhat:

```sh
$ npm run compile
```

### TypeChain

Compile the smart contracts and generate TypeChain artifacts:

```sh
$ npm run typechain
```

### Lint Solidity

Lint the Solidity code:

```sh
$ npm run lint:sol
```

### Lint TypeScript

Lint the TypeScript code:

```sh
$ npm run lint:ts
```

### Test

Run the Chai tests:

```sh
$ npm run test
```

### Coverage

Generate the code coverage report:

```sh
$ npm run coverage
```

### Report Gas

See the gas usage per unit test and average gas per method call:

```sh
$ REPORT_GAS=true npm run test
```

### Clean

Delete the smart contract artifacts, the coverage reports and the Hardhat cache:

```sh
$ npm run clean
```

## Deploy

Deploy the contracts to Hardhat Network:

```sh
$ npm run deploy
```

Deploy the contracts to a specific network, such as the Ropsten testnet:

```sh
$ npm run deploy:network ropsten
```

## Syntax Highlighting

If you use VSCode, you can enjoy syntax highlighting for your Solidity code via the
[vscode-solidity](https://github.com/juanfranblanco/vscode-solidity) extension. The recommended approach to set the
compiler version is to add the following fields to your VSCode user settings:

```json
{
  "solidity.compileUsingRemoteVersion": "v0.8.3+commit.8d00100c",
  "solidity.defaultCompiler": "remote"
}
```

Where of course `v0.8.3+commit.8d00100c` can be replaced with any other version.

## Deploy Arcana Smart Contracts on Polygon Edge network(Local machine)

### Prerequisites
- [Docker](https://docs.docker.com/engine/install/)

Note: Make sure to setup validator node(Polygon Edge) on local machine before deploying Arcana Smart Contracts. Repository link for validator node setup: https://github.com/arcana-network/validator-node-setup

1. Clone the repository

```
git clone git@github.com:arcana-network/arcana-smart-contract.git
```

2. Create environment file

```
cp .env.example .env
```

3. Deploy Arcana Smart Contract on Polygon Edge network(Local machine).

```
make deploy
```

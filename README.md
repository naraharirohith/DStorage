# Centralized bridge

Centralized bridge supports transfer of data from supported Ethereum testnets i.e. Ropsten and Polygon Mumbai to Arcana network. 
- Current implementaion is specific to the arcana private NFT ownership-transfer.
- The bridge does the transfer of file/asset on Arcana whenever there is any transfer of NFT on either Mumbai or Ropsten.

## Usage

## Start the bridge 

```shell
npm run up
```

### Health endpoint 
```shell
npm run server
```
In a new termianl from server, run
```shell
npm run get-health
```

### NFT transfer status
```shell
npm run server
```
In a new termianl from server, run
```shell
npm run status --queryBlock=BLOCK_NO --chainId=CHAIN_ID
 ```
**chainId** for mumbai is 80001, for ropsten is 3.
**queryBlock** is the blockNumber of mint/transfer on the destination chains.

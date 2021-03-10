import json
from web3 import Web3

ganache_url = "HTTP://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))
print(web3.isConnected())
account_1 = "0x1f50Ce666d649A5f442fAF0135E7ce0845c6521C"
account_2 = "0xFE49AAFABd98839B5e4a917B0B27D01DbCbb9e63"
private_key = "86a959b9343880eb9efe0f4e9769b6670d4bef2e957d2cf47e81690a79b83000"
nonce = web3.eth.getTransactionCount(account_1)
print(nonce)
tx = {
	'nonce' : nonce,
	'to' : account_2,
	'value' : web3.toWei(1, 'ether'),
	'gas' : 2000000,
	'gasPrice' : web3.toWei('5', 'gwei'),
}
signed_tx = web3.eth.account.signTransaction(tx, private_key)
tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
print(web3.toHex(tx_hash))
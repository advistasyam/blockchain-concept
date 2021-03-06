import sys
import hashlib
import json

from time import time
from uuid import uuid4

from flask import Flask
from flask.globals import request
from flask.json import jsonify

import requests
from urllib.parse import urlparse

class Blockchain(object):
    difficulty_target = "0000"

    def hash_block(self, block):
        # Fungsi untuk mengubah string menjadi hashed sha256 string
        block_encoded = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_encoded).hexdigest()
    
    def __init__(self):
        self.chain = []
        self.current_transactions = []

        # genesis hash adalah kode hash pertama block
        genesis_hash = self.hash_block("block_pertama")

        self.append_block(
            hash_of_previous_block = genesis_hash,
            nonce = self.proof_of_work(0, genesis_hash, [])
        )
    
    def proof_of_work(self, index, hash_of_previous_block, transactions):
        # Fungsi mining untuk mencari nonce yang tepat dengan difficulty target
        nonce = 0

        while self.valid_proof(index, hash_of_previous_block, transactions, nonce) is False:
            nonce += 1
        
        return nonce
    
    def valid_proof(self, index, hash_of_previous_block, transactions, nonce):
        to_be_validated = f"{index}{hash_of_previous_block}{transactions}{nonce}".encode()

        hash_result = hashlib.sha256(to_be_validated).hexdigest()

        return hash_result[:len(self.difficulty_target)] == self.difficulty_target
    
    def append_block(self, hash_of_previous_block, nonce):
        block = {
            'index': len(self.chain),
            'timestamp': time(),
            'transaction': self.current_transactions,
            'nonce': nonce,
            'hash_of_previous_block': hash_of_previous_block
        }

        # Clear current transaction
        self.current_transactions = []

        self.chain.append(block)
        return block
    
    def add_transaction(self, sender, recipient, amount):
        self.current_transactions.append({
            'amount': amount,
            'recipient': recipient,
            'sender': sender
        })

        return self.last_block['index'] + 1
    
    @property
    def last_block(self):
        return self.chain[-1]

app = Flask(__name__)

# This Node Wallet Address
node_identifier = str(uuid4()).replace("-", "")

blockchain = Blockchain()

# Route API
@app.route('/', methods=["GET"])
def full_chain():
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain)
    }

    return jsonify(response), 200

@app.route('/mine', methods=["GET"])
def mine_block():
    blockchain.add_transaction(
        sender="0", # Prize
        recipient=node_identifier,
        amount=5 # Hadiah Mining 5 Bitcoin
    )

    last_block_hash = blockchain.hash_block(blockchain.last_block)
    index = len(blockchain.chain)
    nonce = blockchain.proof_of_work(index, last_block_hash, blockchain.current_transactions)

    block = blockchain.append_block(last_block_hash ,nonce)

    response = {
        'message': 'A new block has been added',
        'index': block['index'],
        'hash_of_previous_block': block["hash_of_previous_block"],
        'nonce': block["nonce"],
        'transactions': block["transaction"]
    }

    return jsonify(response), 200

@app.route('/transactions/new', methods=["POST"])
def new_transactions():
    values = request.get_json()

    required_fields = ["sender", "recipient", "amount"]
    if not all(k in values for k in required_fields):
        return("Missing Fields", 400)
    
    index = blockchain.add_transaction(
        sender=values["sender"],
        recipient=values["recipient"],
        amount=values["amount"]
    )
    
    response = {'message': f"Transaksi akan dimasukkan ke blok ke {index}"}

    return (jsonify(response), 201)

# Run the app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(sys.argv[1]))
import datetime
import hashlib
import json
from flask import Flask, jsonify, request


class Blockchain:
    #constructor
    def __init__(self):
        # creating chain
        self.chain = []
        # Initializing First Block
        self.create_block(owner="creator", Reg_no='007', proof=0, previous_hash='0')
    
    def create_block(self, owner, Reg_no, proof, previous_hash):
        #creating Dictionary i.e, block
        block = {
            'owner':owner,                          #constant
            'Reg_no': Reg_no,                       #constant
            'index': len(self.chain)+1,             #constant
            'timestamp': str(datetime.datetime.now),#constant
            'proof': proof,                         #Keep changing
            'previous_hash': previous_hash          #constant
        }
        self.chain.append(block)
        return block

    # Proof of work :  We want a fixed number of zeros in our hash to be in our blockchain
    # Eg - 0000shdhwbd#$#%$fdj  So we have 4 zero's in starting of our hash

    def proof_of_work(self, previous_proof):
        new_proof = 1
        check_proof = False

        while check_proof is False:
            # **2 means square
            # encode() always works on String
            hash_val = hashlib.sha256(str(new_proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_val[:4] == '0000':
                check_proof = True
            else :
                new_proof += 1

        return new_proof
    
    # It will take a block and produces a Hash value of it
    def hash(self, block):
        # Block is a dic , dump() convert dic to String, as encode works on str only
        encoded_block = json.dumps(block).encode()
        return hashlib.sha256(encoded_block).hexdigest()

    def is_chain_valid(self, chain):
        previous_block = chain[0]
        block_idx = 1
        while block_idx < len(chain):
            block  = chain[block_idx]
            # It means chain has been modified, Hash has been changed
            if block['previous_hash'] != self.hash(previous_block):
                return False
            
            # Condition 2 : Suppose block hash been changed and some how new hash value is also 
            # same as previous hash, so we will add 1 more difficulty , by verifying proof
            previous_proof = previous_block['proof']
            proof = block['proof']
            hash_val = hashlib.sha256(str(proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_val[:4] != '0000':
                return False
            
            previous_block = block
            block_idx += 1
        
        return True
    
    def get_last_block(self):
        # get_previous_block
        return self.chain[-1]
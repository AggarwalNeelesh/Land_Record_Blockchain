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
            'owner':owner,
            'Reg_no': Reg_no,
            'index': len(self.chain)+1,
            'timestamp': str(datetime.datetime.now),
            'proof': proof,
            'previous_hash': previous_hash
        }
        self.chain.append(block)
        return block

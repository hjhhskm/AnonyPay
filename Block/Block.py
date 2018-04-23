# -*- coding: utf-8 -*-

import hashlib as hasher
import sys
import datetime as dater

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.hash_block()
        pass

    def hash_block(self):
        sha = hasher.sha256()
        text = str(self.index) + str(self.timestamp) + str(self.data.encode("utf-8")) + str(self.previous_hash)
        sha.update(str(text).encode("utf-8"))
        return sha.hexdigest()
    pass

def check_block(recv_block,recv_time,recv_data,pre_hash):
    sha = hasher.sha256()
    text = str(recv_block.index) + str(recv_time) + str(recv_data) + str(pre_hash)
    sha.update(str(text).encode("utf-8"))
    return sha.hexdigest() == recv_block.hash

first_block = Block(0,dater.datetime.now(),"good","32276")
print(first_block.hash,"first block create time is ",first_block.timestamp)
print(check_block(first_block,first_block.timestamp,"bad",first_block.previous_hash))
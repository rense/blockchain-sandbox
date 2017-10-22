from hashlib import sha256
from datetime import datetime


class Block(object):

    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash

    @property
    def hash(self):
        sha = sha256()
        sha.update('{:d}{}{}{}'.format(
            self.index, self.timestamp, self.data, self.previous_hash
        ).encode('utf-8'))
        return sha.hexdigest()

    def __str__(self):
        return "Block <{}>: {}".format(self.hash, self.data)


class Blockchain(object):

    def __init__(self):
        self.blocks = []
        self.add_genesis_block()

    def add_genesis_block(self):
        return self.blocks.append(
            Block(0, datetime.now(), "Genesis block #0", 0)
        )

    def add_block(self, data):
        previous_block = self.blocks[-1]
        block = Block(
            previous_block.index + 1,
            datetime.now(),
            data,
            previous_block.hash
        )
        return self.blocks.append(block)


class Coin(object):

    def __init__(self):
        self.blockchain = Blockchain()

    def populate(self, amount):
        for n in range(1, amount + 1):
            self.blockchain.add_block("Data #{:d}".format(n))

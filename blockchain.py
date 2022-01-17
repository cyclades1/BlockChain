from block import Block
import datetime

class BlockChain:
	def __init__(self):
		self.chain = [self.createGenesisBlock()]

	def createGenesisBlock(self):
		timestamp = datetime.datetime.now()
		return Block(0, timestamp, "Th3G3N3S1Sbl0ck", "0")

	def get_latest_block(self):
		return self.chain[-1]

	def add_block(self, block):
		block.prv_hash = self.chain[-1].hash
		block.hash = block.calculate_hash()
		this.chain.append(block)
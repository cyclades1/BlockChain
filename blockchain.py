from block import Block
import datetime
import json

class BlockChain:
	def __init__(self):
		self.difficulty = 4
		self.chain = [self.createGenesisBlock()]

	def createGenesisBlock(self):
		timestamp = str(datetime.datetime.now())
		g_block =  Block(0, timestamp, "Th3G3N3S1Sbl0ck")
		g_block.minblock(self.difficulty)
		return g_block

	def get_latest_block(self):
		return self.chain[-1]

	def add_block(self, block):
		block.prv_hash = self.chain[-1].hash
		block.minblock(self.difficulty)
		self.chain.append(block)

	def get_length(self):
		return len(self.chain)

	def get_block_by_index(self, index):
		for i in range(self.get_length()):
			if self.chain[i].index == index:
				return self.chain[i]
		return None

	def check_valid(self):
		for i in range(1, self.get_length()):
			curblock = self.chain[i]
			prvblock = self.chain[i-1]
			if curblock.hash != curblock.calculate_hash():
				return False
			if curblock.prv_hash != prvblock.hash:
				return False

		return True


	def toJSON(self):
		return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
		

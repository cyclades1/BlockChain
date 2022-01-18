import datetime
import hmac
import hashlib
import json

class Block:
	def __init__(self, index, timestamp, data, prv_hash= ""):
		self.index = index
		self.timestamp = timestamp
		self.data = data
		self.prv_hash = prv_hash
		self.nonce = 0
		self.hash = self.calculate_hash()
		

	def calculate_hash(self):
		key = " #@th1s_1s_0ur_k3y@# "
		id = str(self.index) + self.prv_hash+ str(self.timestamp)+ str(self.data) +str(self.nonce)
		return hmac.new(key.encode('utf-8'), id.encode('utf-8'), hashlib.sha256).hexdigest()

	def minblock(self, difficulty):
		while self.hash[0:difficulty] != "0"*difficulty:
			self.nonce+=1
			self.hash = self.calculate_hash()

	def toJSON(self):
		return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
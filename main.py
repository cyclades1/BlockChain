from blockchain import BlockChain
from block import Block
from datetime import datetime
import json
from pprint import pprint


class InvalidNumber(Exception):
	def __str__(self):
		return "Invalid Number seleted"


class Main:

	def __init__(self):
		self.Coin = BlockChain()

	def alter(self):
		index = input("Enter index of the block You want to alter..")
		block = self.Coin.get_block_by_index(index)
		if not block:
			print("Invalid block index")
			return
		amount = int(input("Enter new amount"))
		block.amount = amount
		print("amount altered, chain is invalid now")

	def add(self):
		print("Enter number of blocks to add..")
		while True:
			try:
				number = int(input())
				if 11<=number<=0:
					raise InvalidNumber
				break
			except Exception as e:
				print(e)
				print("Valid number range from 1-10")

		for _ in range(number):
			data = {}
			data['sender'] = input("Enter name of sender: ")
			data['receiver'] = input("Enter name of reciver: ")
			while True:
				try:
					amount = int(input("Enter valid integer amount paid.. " ))
					break
				except Exception as e:
					print("Invalid amount")
			data["amount"]= amount
			print()
			index = str(int(self.Coin.get_latest_block().index)+1)
			self.Coin.add_block(Block(index,str(datetime.now()), data))
			print("Added to block..")
			print()

	def runner(self):
		print("Welcome to BlockChain..")
		

		while True:
			print('''
	Options:
		1. Add the block in chain (press 1)
		2. Check lenght of the BlockChain (press 2)
		3. Check validity of the Chain (press 3)
		4. Attempt to alter block in the chain (press 4)
		5. See last inserted block in chain (press 5)
		6. Get whole blockchain info (press 6)
		7. Exit (press 0)
				''')
			try:	
				choice = int(input())
			except Exception as e:
				print("invalid input exiting...")
				continue
			if not choice:
				print("Thank you..")
				break

			if choice == 1:
				self.add()
				
			if choice == 2:
				print("Lenght of the blockchain is.. {}\n".format(self.Coin.get_length()))
				continue

			elif choice == 3:
				print("Chain is valid" if self.Coin.check_valid() else "Chain is not valid")
				print()
				continue
			
			elif choice == 4:
				self.alter()
				print()
				continue
			
			elif choice == 5:
				print("last element : {}\n".format(self.Coin.get_latest_block().toJSON() ))
				continue
			
			elif choice == 6:
				print(self.Coin.toJSON())
				print()
				continue
			
			else:
				print("invalid input...\n")
				continue

		

if __name__ == "__main__":
	Main().runner()
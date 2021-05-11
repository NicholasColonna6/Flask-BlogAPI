# Basic Implementation of the Hash Table data structure

# class to represent linked lists at each index of the hash table
class Node:
	def __init__(self, data=None, next=None):
		self.data = data
		self.next = next

# class to represent key/value pairs as the data within our node/linked-list
class Data:
	def __init__(self, key, value):
		self.key = key
		self.value = value

# class to represent the hash table
class HashTable:
	def __init__(self, table_size):
		self.table_size = table_size
		self.hash_table = [None] * table_size

	# converts a key into a hash value
	def custom_hash(self, key):
		hash_value = 0
		for i in key:
			hash_value += ord(i)
			hash_value = (hash_value * ord(i)) % self.table_size
		return hash_value

	# adds key/value pair to the hash table
	def add_key_value(self, key, value):
		hashed_key = self.custom_hash(key)
		if self.hash_table[hashed_key] is None:
			self.hash_table[hashed_key] = Node(Data(key, value), None)
		else:
			node = self.hash_table[hashed_key]
			while node.next is not None:
				node = node.next
			node.next = Node(Data(key, value), None)

	# retrieves value from hash table given a key, returns None if not there
	def get_value(self, key):
		hashed_key = self.custom_hash(key)
		if self.hash_table[hashed_key] is not None:
			node = self.hash_table[hashed_key]
			if node.next is None:
				return node.data.value
			while node is not None:
				if key == node.data.key:
					return node.data.value
				node = node.next
		return None

	# prints the hash table
	def print_table(self):
		print("{")
		for i, val in enumerate(self.hash_table):
			if val is not None:
				llist_string = ""
				node = val
				if node.next is not None:
					while node is not None:
						llist_string += (str(node.data.key) + " : " + str(node.data.value) + " --> ")
						node = node.next
					llist_string += "None"
					print(f"    [{i}] {llist_string}")
				else:
					print(f"    [{i}] {val.data.key} : {val.data.value}")
			else:
				print(f"    [{i}] {val}")
		print("}")

"""
ht = HashTable(4)
ht.add_key_value("test", "one")
ht.add_key_value("testing", "two")
ht.add_key_value("test", "three")
ht.add_key_value("key", "value")
ht.print_table()
"""
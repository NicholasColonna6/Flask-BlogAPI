class Node:
	def __init__(self, data=None, next=None):
		self.data = data
		self.next = next

class Data:
	def __init__(self, key, value):
		self.key = key
		self.value = value

class HashTable:
	def __init__(self, table_size):
		self.table_size = table_size
		self.hash_table = [None] * table_size

	#converts a key into a hash value
	def custom_hash(self, key):
		hash_value = 0
		for i in key:
			hash_value += ord(i)
			hash_value = (hash_value * ord(i)) % self.table_size
		return hash_value

	def add_key_value(self, key, value):
		hashed_key = self.custom_hash(key)
		if self.hash_table[hashed_key] is None:
			self.hash_table[hashed_key] = Node(Data(key, value), None)
		else:
			node = self.hash_table[hashed_key]
			while node.next is not None:
				node = node.next
			node.next = Node(Data(key, value), None)

	def get_value(self, key):
		hashed_key = self.custom_hash(key)
		if self.hash_table[hashed_key] is not None:
			node = self.hash_table[hashed_key]
			if node.next_node is None:
				return node.data.value
			while node is not None:
				if key == node.data.key:
					return node.data.value
				node = node.next

		return None
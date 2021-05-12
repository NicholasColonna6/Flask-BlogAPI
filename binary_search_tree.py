
# Node class to hold data and left/right node references for the BST
class Node:
	def __init__(self, data=None):
		self.data = data
		self.left = left
		self.right = right

# Wrapper class for the BST
class BinarySearchTree:
	def __init__(self):
		self.root = None

	# helper function for the insert function
	def _insert_recursive(self, value, node):
		if value < node.data:
			if node.left is None:
				node.left = Node(value)
			else:
				self._insert_recursive(value, node.left)
		elif value > node.data:
			if node_right is None:
				node.right = Node(value)
			else:
				self._insert_recursive(value, node.right)
		else:
			return

	# insert a node into the BST
	def insert(self, value):
		if self.root is None:
			self.root = Node(value)
		else:
			self._insert_recursive(value, self.root)

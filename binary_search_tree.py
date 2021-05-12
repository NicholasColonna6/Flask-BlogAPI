# Basic Implementation of the Binary Search Tree data structure

# Node class to hold data and left/right node references for the BST
class Node:
	def __init__(self, data=None):
		self.data = data
		self.left = None
		self.right = None

# Wrapper class for the BST
class BinarySearchTree:
	def __init__(self):
		self.root = None

	# helper function for the insert function
	def _insert_recursive(self, data, node):
		if data["id"] < node.data["id"]:
			if node.left is None:
				node.left = Node(data)
			else:
				self._insert_recursive(data, node.left)
		elif data["id"] > node.data["id"]:
			if node.right is None:
				node.right = Node(data)
			else:
				self._insert_recursive(data, node.right)
		else:
			return

	# insert a node into the BST
	def insert(self, data):
		if self.root is None:
			self.root = Node(data)
		else:
			self._insert_recursive(data, self.root)


	# helper function for the search function
	def _search_recursive(self, blog_post_id, node):
		if node is None:
			return False
		elif blog_post_id == node.data["id"]:
			return node.data
		elif blog_post_id < node.data["id"]:
			return self._search_recursive(blog_post_id, node.left)
		else:
			return self._search_recursive(blog_post_id, node.right)

	# search the BST for a particular node
	def search(self, blog_post_id):
		blog_post_id = int(blog_post_id)
		if self.root is None:
			return False
		else:
			return self._search_recursive(blog_post_id, self.root)
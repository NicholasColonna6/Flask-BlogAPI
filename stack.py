# Basic implementation of the Stack data structure

# class to hold data and references for the Stack
class Node:
	def __init__(self, data, next=None):
		self.data = data
		self.next = next

# class to represent the Stack data structure
class Stack:
	def __init__(self):
		self.head = None

	# return the top node in the stack (without removing)
	def peek(self):
		return self.head

	# add new node to top of stack
	def push(self, data):
		next_node = self.head
		self.head = Node(data, next_node)

	# remove the node at the top of the stack
	def pop(self):
		if self.head is None:
			return None
		else:
			temp = self.head
			self.head = self.head.next
			return temp
# Basic implementation of the Queue data structure

# class to hold data and reference to next node of queue
class Node:
	def __init__(self, data, next=None):
		self.data = data
		self.next = next

# class to represent the queue data structure
class Queue:
	def __init__(self):
		self.head = None
		self.tail = None

	# add node to the queue (append to end)
	def enqueue(self, data):
		if self.head is None and self.tail is None:
			self.head = Node(data)
			self.tail = self.head
		else:
			self.tail.next = Node(data, None)
			self.tail = self.tail.next

	# remove next node from the queue (first node)
	def dequeue(self):
		if self.head is None:
			return None
		else:
			temp = self.head
			self.head = self.head.next
			if self.head is None:
				self.tail = None
			return temp
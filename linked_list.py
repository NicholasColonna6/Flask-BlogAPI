class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        self.last_node = None

    def print_ll(self):
        ll_string = ""
        node = self.head
        if node is None:
            print(None)
        while node is not None:
            ll_string += f"{str(node.data)} -> "
            node = node.next
        ll_string += "None"
        print(ll_string)

    def to_list(self):
        lst = []
        if self.head is None:
            return lst
        
        node = self.head
        while node is not None:
            lst.append(node.data)
            node = node.next
        return lst

    def insert_beginning(self, data):
        if self.head is None:
            self.head = Node(data, None)
            self.last_node = self.head
        
        new_node = Node(data, self.head)
        self.head = new_node

    # By keeping track of 'last_node', we can insert at end in O(1) time rather than O(n)
    def insert_at_end(self, data):
        if self.head is None:
            self.insert_beginning(data)

        self.last_node.next = Node(data, None)
        self.last_node = self.last_node.next
# Basic Implementation of the Linked List data structure

# class to represent nodes within a linked list
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

# class to represent linked list
class LinkedList:
    def __init__(self):
        self.head = None    # keep track of first node (head) of linked list
        self.last_node = None   # keep track of last node (tail) of linked list

    # Print linked list data in order
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

    # Convert Linked List to a List
    def to_list(self):
        lst = []
        if self.head is None:
            return lst
        
        node = self.head
        while node is not None:
            lst.append(node.data)
            node = node.next
        return lst

    # Insert a node at the beginning of a linked list
    def insert_beginning(self, data):
        if self.head is None:
            self.head = Node(data, None)
            self.last_node = self.head
        else:
            new_node = Node(data, self.head)
            self.head = new_node

    # Insert a node at the end of a linked list
    # By keeping track of 'last_node', we can insert at end in O(1) time rather than O(n)
    def insert_at_end(self, data):
        if self.head is None:
            self.insert_beginning(data)

        self.last_node.next = Node(data, None)
        self.last_node = self.last_node.next

    # Retrieve a user from a linked list based on a given user_id
    def get_user_by_id(self, user_id):
        node = self.head
        while node is not None:
            if node.data["id"] == int(user_id):
                return node.data
            node = node.next
        return None
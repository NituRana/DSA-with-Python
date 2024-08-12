'''
Introduction to Doubly Linked List (DLL)
A Doubly Linked List (DLL) is a type of linked list where each node contains three fields:

Data Field: Stores the actual data.
Next Pointer: Points to the next node in the list.
Previous Pointer: Points to the previous node in the list.
Unlike a singly linked list, where each node points only to the next node, a doubly linked list allows 
traversal in both directions (forward and backward), thanks to the additional pointer to the previous node.

Structure of a Doubly Linked List Node
In a doubly linked list, each node is typically represented using a structure or class with three fields:

data: The value stored in the node.
next: A reference to the next node in the list.
prev: A reference to the previous node in the list.

'''


# Node class represents each element in the doubly linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

# Doubly Linked List class contains methods to manipulate the list
class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # Method to append a new node at the end of the list
    def append_in_dll(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        new_node.prev = last

    # Method to insert a new node at the beginning of the list
    def prepend(self, data):
            new_node = Node(data)
            if self.head is None:
                self.head = new_node
                return
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node

    # method for the display DLL nodes
    def display(self):
            # Initialize an empty list to store node data
            node_list = []
            temp = self.head
            # Traverse the list and collect data from each node
            while temp:
                node_list.append(temp.data)
                temp = temp.next

            print(f"These are the elements of DLL :{node_list}")


dll = DoublyLinkedList()
dll.append_in_dll(5)
dll.append_in_dll(3)
dll.display()

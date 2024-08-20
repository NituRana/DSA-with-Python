'''
Problem Statement: Given a doubly linked list of size N consisting of positive integers, your task is to reverse it and return the head of the modified doubly linked list.

Examples
Example 1:

Input Format:

DLL: 1 <-> 2 <-> 3 <-> 4
Result: DLL: 4 <-> 3 <-> 2 <-> 1

'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        new_node.prev = last

    def reverse(self):
        current = self.head
        temp = None
        while current:
            # Swap the next and prev pointers for each node
            temp = current.prev
            current.prev = current.next
            current.next = temp
            
            # Move to the next node in the original order, which is now the previous node
            current = current.prev
        
        # Adjust the head of the list to the last node, which is now the first node
        if temp:
            self.head = temp.prev

    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        print(" -> ".join(map(str, elements)))

# Example usage:
dll = DoublyLinkedList()
dll.append(1)
dll.append(2)
dll.append(3)
dll.append(4)
dll.append(5)

print("Original Doubly Linked List:")
dll.display()

dll.reverse()

print("Reversed Doubly Linked List:")
dll.display()
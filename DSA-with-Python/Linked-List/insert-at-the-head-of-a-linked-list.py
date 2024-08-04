'''

Problem Statement:  Given a linked list and an integer value val, insert a new node with that value at the beginning (before the head) of the list and return the updated linked list.

Examples
Solution
Disclaimer: Don't jump directly to the solution, try it out yourself first.

Approach:
To insert a new node with a value before the head of the list, create a new node with the given value val pointing to the head. This node will be the new head of the linked list.

Algorithm:
Create a new node with data as the given value and pointing to the head. This node will be our new head of the linked list.

'''

class Node:
    def __init__(self, data1, next1=None):
        self.data = data1
        self.next = next1

def printLL(head):
    while head is not None:
        print(head.data, end=" ")
        head = head.next

def insertHead(head, val):
    temp = Node(val, head)
    return temp

if __name__ == "__main__":
    arr = [12, 8, 5, 7]
    val = 100

    head = Node(arr[0])
    head.next = Node(arr[1])
    head.next.next = Node(arr[2])
    head.next.next.next = Node(arr[3])

    head = insertHead(head, val)

    printLL(head)


# Define the Node and LinkedList Classes

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
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

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def insert_in_middle(self, data):
        # Create a new node with the data
        new_node = Node(data)
        
        # If the list is empty, the new node becomes the head
        if not self.head:
            self.head = new_node
            return

        # Use the slow and fast pointer technique to find the middle
        slow = self.head
        fast = self.head
        prev = None

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        # Insert the new node in the middle
        new_node.next = slow

        if prev:
            prev.next = new_node
        else:
            # If prev is None, it means the list had only one node
            self.head = new_node
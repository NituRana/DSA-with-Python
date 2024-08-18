'''
Problem Statement: Given the head of a linked list, print the length of the linked list.

Example 1:

Input Format: 0->1->2

Result: 3

Explanation: The list has a total of 3 nodes, thus the length of the list is 3.
'''

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def append_in_linked_list(self, data):
        new_node = Node(data)
        temp = self.head
        if temp is None:
            self.head = new_node
            return
        if temp.next:
            while temp:
                temp = temp.next
        temp.next = new_node
        return
    def check_the_length_of_the_ll(self):
        count = 0
        temp = self.head
        if temp is not None:
            while temp:
                temp = temp.next
                count += 1
            print(f"There are {count} elements in linked list.")

        else:
            print("Linked list is empty.")

ll = LinkedList()
ll.append_in_linked_list(9)
ll.append_in_linked_list(4)
ll.check_the_length_of_the_ll()
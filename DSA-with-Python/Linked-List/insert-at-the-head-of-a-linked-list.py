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
'''
Linked Lists: In-Depth Explanation
1. What is a Linked List?

A linked list is a linear data structure where elements, called nodes, are stored in a sequence, but unlike arrays, elements are not stored in 
contiguous memory locations. Each node in a linked list contains two parts:

'Data': The value or information the node holds.
'Pointer (or Reference)': A reference to the next node in the sequence.
Linked lists are dynamic data structures that can grow and shrink during runtime, making them more flexible than arrays.

Each node in a linked list holds a piece of data and a reference to the next node in the list. The first node is called the head. 
Traversing the linked list involves starting from the head and following the next pointers until reaching a node where the next pointer 
is null (or back to the head in a circular linked list).



'''
class Node:
    def __init__(self, data1, next1=None):
        self.data = data1
        self.next = next1
# Creating a Node 'x' with the first element of the array
x = Node(2)
# Creating a reference 'y' pointing to the same Node 'x'
y = x
# Printing the reference 'y', which represents the memory address of the Node 'x'
print(y)
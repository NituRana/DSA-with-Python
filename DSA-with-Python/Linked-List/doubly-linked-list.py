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


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

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

    # def prepend(self, data):
    #         new_node = Node(data)
    #         if self.head is None:
    #             self.head = new_node
    #             return
    #         self.head.prev = new_node
    #         new_node.next = self.head
    #         self.head = new_node

    # def deletion_in_dll(self, node):
    #     temp = self.head
    #     if temp is not None:
    #         if temp.data == node:
    #             self.head = temp.next
    #             if self.head:
    #                 self.head.prev = None
    #             return

    #     while temp is not None:
    #         if temp.data == node:
    #             break
    #         temp = temp.next

    #     if temp is None:
    #         return
        
    #     if temp.next is not None:
    #         temp.next.prev = temp.prev

    #     if temp.prev is not None:
    #         temp.prev.next = temp.next


    def display(self):
        node_list = []
        temp = self.head
        while temp:
            node_list.append(temp.data)
            temp = temp.next

        print(f"These are the elements of DLL :{node_list}")


dll = DoublyLinkedList()
dll.append_in_dll(5)
dll.append_in_dll(3)
dll.append_in_dll(8)
# dll.deletion_in_dll(3)
# dll.prepend(0)
# dll.append_in_dll(4)
dll.display()

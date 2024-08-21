'''
Problem Statement: Given a doubly linked list of size N consisting of positive integers, your task is to reverse it and return the head of the modified doubly linked list.

Examples
Example 1:

Input Format:

DLL: 1 <-> 2 <-> 3 <-> 4
Result: DLL: 4 <-> 3 <-> 2 <-> 1

'''

# Approach one use stack :

class Node:
    def __init__(self, data):
        self.back = None
        self.data = data
        self.next = None

class Doubly_linkend_list:
    def __init__(self):
        self.head = None
    
    def append_in_dll(self, data):
        new_node = Node(data)
        temp = self.head
        if temp is None:
            self.head = new_node
            return
        if temp.next:
            while temp.next:
                temp = temp.next
        temp.next = new_node
        new_node.back = temp
        return
    
    def reverse_in_dll_using_stack(self):
        temp = self.head
        stack = []
        if temp is None:
            print("dll is empty.")
            return
        if temp.next:
            while temp:
                stack.append(temp.data)
                temp = temp.next
            temp_2 = self.head
            while temp_2:
                temp_2.data = stack.pop()
                temp_2 = temp_2.next
        return
    
    def display_ele_of_dll(self):
        temp = self.head
        arr_of_ele = []
        if temp:
            while temp:
                arr_of_ele.append(temp.data)
                temp = temp.next
            print(" Dll elements :", arr_of_ele)
            return arr_of_ele
        else:
            print("No element on the dll.")
            return

dll = Doubly_linkend_list()
dll.append_in_dll(72)
dll.append_in_dll(6)
dll.append_in_dll(34)
dll.append_in_dll(21)
dll.display_ele_of_dll()
dll.reverse_in_dll_using_stack()
dll.display_ele_of_dll()



# Approach change the links (more optimal way):

class Node:
    def __init__(self, data):
        self.data = data
        self.back = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
    
    def append_in_dll(self, data):
        new_node = Node(data)
        temp = self.head
        if temp is None:
            self.head = new_node
            return
        if temp.next:
            while temp.next:
                temp = temp.next
        temp.next = new_node
        new_node.back = temp
        return
    def reverse_in_dll(self):
        temp = self.head
        if temp is None:
            print(" Dll is empty.")
            return
        while temp:
            next_node = temp.next
            temp.next = temp.back
            temp.back = next_node

            # Move temp to the previous node (which is now temp.prev after the swap)
            if temp.back is None:  # If we're at the end of the list, this will be the new head
                self.head = temp
            temp = temp.back  # Move to the next node in the original list order
        return
    def dispaly_elements_of_dll(self):
        temp = self.head
        arr_of_ele = []
        if temp is None:
            print("DLL is empty.")
            return
        while temp:
            arr_of_ele.append(temp.data)
            temp = temp.next
        print(" Dll_2 elements :", arr_of_ele)
        return arr_of_ele

dll_2 = DoublyLinkedList()
dll_2.append_in_dll(72)
dll_2.append_in_dll(6)
dll_2.append_in_dll(34)
dll_2.append_in_dll(21)
dll_2.dispaly_elements_of_dll()
dll_2.reverse_in_dll()
dll_2.dispaly_elements_of_dll()

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#         self.prev = None

# class DoublyLinkedList:
#     def __init__(self):
#         self.head = None

#     def append(self, data):
#         new_node = Node(data)
#         if not self.head:
#             self.head = new_node
#             return
#         last = self.head
#         while last.next:
#             last = last.next
#         last.next = new_node
#         new_node.prev = last

#     def reverse(self):
#         current = self.head
#         temp = None
#         while current:
#             # Swap the next and prev pointers for each node
#             temp = current.prev
#             current.prev = current.next
#             current.next = temp
            
#             # Move to the next node in the original order, which is now the previous node
#             current = current.prev
        
#         # Adjust the head of the list to the last node, which is now the first node
#         if temp:
#             self.head = temp.prev

#     def display(self):
#         elements = []
#         current = self.head
#         while current:
#             elements.append(current.data)
#             current = current.next
#         print(" -> ".join(map(str, elements)))

# # Example usage:
# dll = DoublyLinkedList()
# dll.append(1)
# dll.append(2)
# dll.append(3)
# dll.append(4)
# dll.append(5)

# print("Original Doubly Linked List:")
# dll.display()

# dll.reverse()

# print("Reversed Doubly Linked List:")
# dll.display()
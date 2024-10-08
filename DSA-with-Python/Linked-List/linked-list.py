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

'''-------------------------------------------------------------
class Node:
    def __init__(self, data1, next1=None):
        self.data = data1
        self.next = next1
# Creating a Node 'x' with the first element of the array
x = Node(2)
print("---------------------- x:", x)
# Creating a reference 'y' pointing to the same Node 'x'
y = x
# Printing the reference 'y', which represents the memory address of the Node 'x'
print(y)

class LinkedList:
    def __init__(self):
        self.head = None

    def append_in_ll(self, data):
        new_node = Node(data)
        last_node = self.head
        if last_node is None:
            self.head = new_node
            return
        if last_node.next:
            while last_node.next:
                last_node = last_node.next
        last_node.next = new_node
        return
    
    def prepend_in_ll(self, data):
        new_node = Node(data)
        first_node = self.head
        if first_node is None:
            self.head = new_node
            return
        self.head = new_node
        new_node.next = first_node
        return


    def deletiona_in_ll(self, data):
        temp = self.head
        if temp is not None:
            if temp.data == data:
                self.head = temp.next
            if temp.next is not None:
                while temp.next:
                    if temp.data == data:
                        self.head = temp.next
                        return
                    temp = temp.next
            else:
                return ("This element not persent in Linked List")



    
    def display_elements_of_ll(self):
        arr_of_ele = []
        temp_node = self.head
        while temp_node:
            arr_of_ele.append(temp_node.data)
            temp_node =temp_node.next
        
        print(f"These are the elements of the linked list : {arr_of_ele}")
    
ll = LinkedList()
ll.append_in_ll(9)
ll.append_in_ll(4)
ll.display_elements_of_ll()
ll.prepend_in_ll(0)
ll.display_elements_of_ll()
ll.deletiona_in_ll(0)
ll.prepend_in_ll(18)
ll.prepend_in_ll(10)
ll.display_elements_of_ll()

-----------------------------------------------------'''

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def append_in_ll(self, data):
#         new_node = Node(data)
#         curr_node = self.head
#         if curr_node is None:
#             self.head = new_node
#             return 
#         if curr_node.next is None:
#             curr_node.next = new_node
#             return
#         while curr_node.next:
#             curr_node = curr_node.next
#         curr_node.next = new_node
#         return
    
#     def prepend_in_ll(self, data):
#         new_node = Node(data)
#         curr_node = self.head
#         if curr_node is None:
#             self.head = new_node
#             return
#         self.head = new_node
#         new_node.next = curr_node
#         return
        

#     def deletion_in_ll(self, data):
#         curr_node = self.head
#         if curr_node is None:
#             return "their is no elements in linked list."
#         prev_node = None
#         while curr_node:
#             if curr_node.data == data:
#                 prev_node.next = curr_node.next
#             prev_node = curr_node
#             curr_node = curr_node.next
#         return

    
#     def display_in_ll(self):
#         curr_node = self.head
#         array_of_elements = []
#         while curr_node:
#             array_of_elements.append(curr_node.data)
#             curr_node = curr_node.next
#         return array_of_elements

# ll = LinkedList()
# ll.prepend_in_ll(3)
# ll.append_in_ll(9)
# ll.append_in_ll(4)
# ll.prepend_in_ll(0)
# ll.prepend_in_ll(8)
# ll.append_in_ll(5)
# ll.deletion_in_ll(3)
# ll.append_in_ll(2)
# print("----------display_the_ele_of_ll 1:--------- ", ll.display_in_ll())
# print("----------deletion_in_ll :--------- ", ll.deletion_in_ll(4))
# print("----------display_the_ele_of_ll 2:--------- ", ll.display_in_ll())

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append_in_linked_list(self, data):
        curr_node = self.head
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return True
        while curr_node.next:
            curr_node = curr_node.next
        curr_node.next = new_node
        return True
    
    def display_in_linked_list(self):
        arr_of_ele = []
        curr_node = self.head
        while curr_node:
            arr_of_ele.append(curr_node.data)
            curr_node = curr_node.next
        print(f"----------- linked list elements: {arr_of_ele}")
        return arr_of_ele

ll = LinkedList()
ll.append_in_linked_list(2)
ll.append_in_linked_list(7)
ll.append_in_linked_list(3)
ll.append_in_linked_list(9)
ll.display_in_linked_list()
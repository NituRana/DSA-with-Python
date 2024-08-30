'''
Reverse a Linked List

Problem Statement: Problem Statement: Given the head of a singly linked list, write a program to reverse the linked list, and return the head pointer to the reversed list.

Example 1:

Input Format:

LL: 1   3   2   4 

LL: 4   3   2   1
'''
# Approach one (using stack)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
    
class LinkedList:
    def __init__(self):
        self.head = None
    
    def append_in_ll(self, data):
        new_node = Node(data)
        current_node = self.head
        if current_node is None:
            self.head = new_node
            return
        if current_node.next:
            while current_node.next:
                current_node = current_node.next
        current_node.next = new_node
        return
    
    def reverse_in_ll(self):
        ele_stack = []
        current_node = self.head
        if current_node is None:
            print("The Linked List is emplty.")
            return
        while current_node:
            ele_stack.append(current_node.data)
            current_node = current_node.next
        rev_node = self.head
        while rev_node:
            rev_node.data = ele_stack.pop()
            rev_node = rev_node.next
        return
    
    def dispaly_the_elements_of_ll(self):
        temp = self.head
        list_of_ll_elements = []
        while temp:
            list_of_ll_elements.append(temp.data)
            temp = temp.next
        print(" Linked Lis elements : ", list_of_ll_elements)
        return


ll = LinkedList()
ll.append_in_ll(98)
# ll.append_in_ll(6)
# ll.append_in_ll(43)
# ll.append_in_ll(51)
ll.dispaly_the_elements_of_ll()
ll.reverse_in_ll()
ll.dispaly_the_elements_of_ll()


# Appoarch second by changing the links or address part


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LiskedListTwo:
    def __init__(self):
        self.head = None
    
    def append_in_ll(self, data):
        new_node = Node(data)
        current_node = self.head
        if current_node is None:
            self.head = new_node
            return
        if current_node.next:
            while current_node.next:
                current_node = current_node.next
        current_node.next = new_node
        return
    
    def reverse_in_ll(self):
        temp = self.head
        if temp is None:
            print("The given Linked List is empty.")
            return
        if temp.next:
            prev_node = None
            while temp:
                next_node = temp.next
                temp.next = prev_node
                prev_node = temp
                # if temp.next is None:
                #     self.head = temp
                temp = next_node
            self.head = prev_node
        return

    def dispaly_the_elements_of_ll(self):
        temp = self.head
        list_of_ll_elements = []
        while temp:
            list_of_ll_elements.append(temp.data)
            temp = temp.next
        print(" Linked List two elements : ", list_of_ll_elements)
        return
            
ll = LiskedListTwo()
ll.append_in_ll(98)
# ll.append_in_ll(6)
# ll.append_in_ll(43)
# ll.append_in_ll(51)
ll.dispaly_the_elements_of_ll()
ll.reverse_in_ll()
ll.dispaly_the_elements_of_ll()


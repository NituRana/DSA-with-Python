'''
Sort a Linked List

Problem Statement: Given a linked list, sort its nodes based on the data value in them. Return the head of the sorted linked list.

Example 1:

Input:Linked List: 3 4 2 1 5
Output:Sorted List: 1 2 3 4 5

Explanation:  The input linked list when sorted from [3, 4, 2, 1, 5] results in a linked list with values: [1, 2, 3, 4, 5].
'''

# Approach one (using array)

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
    def sort_in_list(self, lst):
        for i in range(len(lst)):
            for j in range(i + 1, len(lst)):
                if lst[i] > lst[j]:
                    temp = lst[j]
                    lst[j] = lst[i]
                    lst[i] = temp
        return lst
    def sorting_in_ll(self):
        ele_list = []
        current_node = self.head
        if current_node is None:
            print("The Linked List is emplty.")
            return
        while current_node:
            ele_list.append(current_node.data)
            current_node = current_node.next
        rev_node = self.head
        ele_list = self.sort_in_list(ele_list)
        while rev_node:
            rev_node.data = ele_list.pop()
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
ll.append_in_ll(6)
ll.append_in_ll(43)
ll.append_in_ll(7)
ll.append_in_ll(51)
ll.dispaly_the_elements_of_ll()
ll.sorting_in_ll()
ll.dispaly_the_elements_of_ll()
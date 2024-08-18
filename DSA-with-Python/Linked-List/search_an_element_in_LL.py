'''
Problem Statement: Given the head of a linked list and an integer value, find out whether the integer is present in the linked list or not. Return true if it is present, or else return false.

Examples
Example 1:

Input Format: 0->1->2, val = 2

Result True

Explanation: Since element 2 is present in the list, it will return true.

Example 2:

Input Format: 12->5->8->7, val = 6 

Result False

Explanation: The list does not contain element 6. Therefore, it returns false.

'''

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class Linked_list:
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
                last_node = last_node
                last_node = last_node.next
        last_node.next = new_node
        return

    def is_the_element_present(self, data):
        temp = self.head
        if temp is not None:
            if temp.data == data:
                print("This element is present in the linked list.")
                return

            if temp.next is not None:
                while temp:
                    if temp.data == data:
                        print("This element is present in the linked list.")
                        return
                    temp = temp.next
                print("This element is not present in the linked list.")
                return 
            else:
                print("This element is not present in the linked list.")
                return

        else:
            print("Lisked list have no elements")
            return
        
    def display_elements_of_ll(self):
        arr_of_ele = []
        temp_node = self.head
        while temp_node:
            arr_of_ele.append(temp_node.data)
            temp_node =temp_node.next
        
        print(f"These are the elements of the linked list : {arr_of_ele}")

ll = Linked_list()
ll.append_in_ll(9)
ll.append_in_ll(4)
ll.append_in_ll(18)
ll.append_in_ll(10)
ll.display_elements_of_ll()
ll.is_the_element_present(10)






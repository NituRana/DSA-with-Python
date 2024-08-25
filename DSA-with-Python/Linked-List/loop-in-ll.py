'''
Length of Loop in Linked List
Problem Statement: Given the head of a linked list, determine the length of a loop present in the linked list; if not present, return 0.

Example 1:

Input Format:
LL: 1  2  3  4  5 
Output: 3

Explanation: A cycle exists in the linked list starting at node 3 -> 4 -> 5 and then back to 3. There are 3 nodes present in this cycle.

Example 2:
Input Format:
LL: 1  2  3  4  9  9
Output: 0

Explanation: In this example, the linked list is linear and does not have a loop hence return 0.
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def create_loop(self, position):
        """Utility function to create a loop in the linked list for testing."""
        if position == 0:
            return
        
        loop_node = self.head
        for i in range(position):
            loop_node = loop_node.next

        last = self.head
        while last.next:
            last = last.next
        last.next = loop_node

    def find_loop_length(self):
        visited = {}
        current = self.head
        
        while current:
            if current in visited:
                # Loop detected, now calculate the loop length
                loop_start = current
                loop_length = 1
                current = current.next
                while current != loop_start:
                    loop_length += 1
                    current = current.next
                return loop_length
            
            visited[current] = True
            current = current.next
        
        return 0

ll1 = LinkedList()
ll1.append(1)
ll1.append(2)
ll1.append(3)
ll1.append(4)
ll1.append(5)

ll1.create_loop(2)

loop_length = ll1.find_loop_length()
print(loop_length)

ll2 = LinkedList()
ll2.append(1)
ll2.append(2)
ll2.append(3)
ll2.append(4)
ll2.append(9)
ll2.append(9)

loop_length = ll2.find_loop_length()
print(loop_length)
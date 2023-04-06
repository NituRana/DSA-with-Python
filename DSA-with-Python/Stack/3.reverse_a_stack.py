'''*******************************************************************************************************
Reverse the given element using stack.

Input : 1, 2, 3
Output : 3, 2, 1

***********************************************************************************************************'''
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

def reverse_stack(stack):
    if not stack.is_empty():
        temp = stack.pop()
        reverse_stack(stack)
        insert_at_bottom(stack, temp)

def insert_at_bottom(stack, item):
    if stack.is_empty():
        stack.push(item)
    else:
        temp = stack.pop()
        insert_at_bottom(stack, item)
        stack.push(temp)

s = Stack()
s.push(1)
s.push(2)
s.push(3)
print("Original stack:", s.items)
reverse_stack(s)
print("Reversed stack:", s.items)

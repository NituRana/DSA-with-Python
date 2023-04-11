'''*******************************************************************************************************
stack using a queue:-

***********************************************************************************************************'''
class Stack:
    def __init__(self):
        self.queue = []
    
    def push(self, item):
        self.queue.append(item)
        for i in range(len(self.queue)-1):
            self.queue.append(self.queue.pop(0))
    
    def pop(self):
        if not self.queue:
            raise IndexError('Stack is empty')
        return self.queue.pop()

s = Stack()
s.push(1)
s.push(2)
s.push(3)
print(s.pop())
print(s.pop())
print(s.pop())






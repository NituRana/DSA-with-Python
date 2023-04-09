'''*******************************************************************************************************
Find the queue using a stack:-

***********************************************************************************************************'''
class Queue:
    def __init__(self):
        self.inbox = []
        self.outbox = []
    
    def enqueue(self, item):
        self.inbox.append(item)
    
    def dequeue(self):
        if not self.outbox:
            while self.inbox:
                self.outbox.append(self.inbox.pop())
        if not self.outbox:
            raise IndexError('Queue is empty')
        return self.outbox.pop()
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())






'''*******************************************************************************************************
Perform the enqueue and dequeue in queue:- 

***********************************************************************************************************'''


class Queue:
    def __init__(self):
        self.items = []
        self.outbox = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.outbox:
            return self.items.pop(0)


q = Queue()
q.enqueue(27)
q.enqueue(98)

print(q.dequeue())
print(q.dequeue())

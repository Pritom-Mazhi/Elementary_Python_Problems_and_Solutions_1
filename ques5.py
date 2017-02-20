class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

q = Queue()

print(q.isEmpty())
q.enqueue(18)
q.enqueue('someString')
q.enqueue(True)
print(q.dequeue())
print(q.dequeue())
print(q.size())

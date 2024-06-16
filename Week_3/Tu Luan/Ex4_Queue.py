class MyQueue():
    def __init__(self, capacity: int):
        self.items = []
        self.capacity = capacity

    def is_full(self):
        return len(self.items) == self.capacity

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, value):
        self.items.append(value)

    def dequeue(self):
        if not self.is_empty():
            remove_item = self.items[0]
            self.items.remove(self.items[0])
            return remove_item

    def front(self):
        if not self.is_empty():
            return self.items[0]


queue1 = MyQueue(5)
queue1.enqueue(1)
queue1.enqueue(2)
print(queue1.is_full())
print(queue1.front())
print(queue1.dequeue())
print(queue1.front())
print(queue1.dequeue())
print(queue1.is_empty())

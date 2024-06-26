class MyStack():
    def __init__(self, capacity: int):
        self.items = []
        self.capacity = capacity
        
    def is_full(self):
        return len(self.items) == self.capacity
    
    def is_empty(self):
        return len(self.items) == 0

    def push(self, value):
        self.items.append(value)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def top(self):
        if not self.is_empty():
            return self.items[-1]

stack1= MyStack(5)
stack1.push(1)
stack1.push(2)
print(stack1.is_full())
print(stack1.top())    
print(stack1.pop())  
print(stack1.top())    
print(stack1.pop())   
print(stack1.is_empty())   
    
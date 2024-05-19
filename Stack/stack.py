from collections import deque


class Stack:
    def __init__(self):
        self.container = deque()
        
    def push(self, val):
        self.container.append(val)
        
    def peek(self):
        return self.container[-1]
        
    def pop(self):
        self.container.pop()
        
    def is_empty(self):
        return len(self.container) == 0
    
    def size(self):
        return len(self.container)
    

s = Stack()

s.push('google.com')
s.push('amazon.com')
s.push('flipkart.com')
print(s.size())
s.pop()
print(s.size())
print(s.peek())
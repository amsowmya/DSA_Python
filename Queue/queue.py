from collections import deque


class Queue:
    def __init__(self):
        self.buffer = deque()
        
    def enqueue(self, val):
        self.buffer.appendleft(val)
        
    def deque(self):
        return self.buffer.pop()
        
    def is_empty(self):
        return len(self.buffer) == 0
    
    def size(self):
        return len(self.buffer)
    
    
q = Queue()

q.enqueue('google.com')
q.enqueue('amazon.com')
q.enqueue('flipkart.com')

print(q.deque())

print(q.size())
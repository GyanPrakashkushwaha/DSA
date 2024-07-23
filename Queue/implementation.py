from collections import deque

class Queue:
    def __init__(self):
        # this deque is a linkedList library in python.
        self.obj = deque()
        
    def enqueue(self,data):
        self.obj.appendleft(data)
        
    def is_empty(self):
        return len(self.obj) == 0
    
    def size(self):
        return len(self.obj)
    
    def dequeue(self):                                       
        return self.obj.pop()
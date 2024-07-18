"""Stack using LinkedList"""

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
class Stack:
    def __init__(self):
        self.head = None
        self.size = -1
    
    def is_empty(self):
        return self.head is None
    
    def push(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.size+=1
        
    def pop(self):
        if self.is_empty():
            raise IndexError('pop from an empty stack')
        popped_value = self.head.data
        self.head = self.head.next
        self.size -= 1
        
        return popped_value
    
    def peek(self):
        if self.is_empty():
            raise IndexError("peek from an empty stack")
        return self.head.data
    
    def size_stack(self):
        return self.size
    
    def __str__(self):
        current = self.head
        items = []
        while current:
            items.append(current.data)
            current = current.next
        return str(items)
    

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack)       # Output: [3, 2, 1]
print(stack.pop()) # Output: 3
print(stack.peek()) # Output: 2
print(stack.size_stack()) # Output: 2
print(stack)       # Output: [2, 1]
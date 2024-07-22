class MyQueue:
    def __init__(self):
        self.ll = []
    
    def push(self, x):
        self.ll.append(x)  # Push at tail
    
    def pop(self):
        front_element = self.ll[0]
        del self.ll[0]  # Pop from head
        return front_element
    
    def peek(self):
        return self.ll[0]
    
    def empty(self):
        return len(self.ll) == 0

# Example usage
if __name__ == "__main__":
    my_queue = MyQueue()
    my_queue.push(1)
    my_queue.push(2)
    print(my_queue.pop())    # returns 1
    print(my_queue.peek())   # returns 2
    print(my_queue.empty())  # returns False

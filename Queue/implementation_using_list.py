
class MyQueue:
    def __init__(self):
        self.arr = []
        self.front = 0

    def push(self, x: int) -> None:
        self.arr.append(x)

    def pop(self) -> int:
        front_element = self.arr[self.front]
        self.front += 1
        return front_element

    def peek(self) -> int:
        return self.arr[self.front]

    def empty(self) -> bool:
        return self.front == len(self.arr)

# Example usage
if __name__ == "__main__":
    myQueue = MyQueue()
    myQueue.push(1)
    myQueue.push(2)
    print(myQueue.peek())    # returns 1
    print(myQueue.pop())     # returns 1
    print(myQueue.empty())   # returns False

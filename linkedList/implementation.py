class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def is_empty(self) -> bool:
        return self.head is None

    def append(self, val) -> None:
        new_node = Node(val)
        if self.is_empty():
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def delete(self, val):
        if self.is_empty():
            return "Can't delete from an empty list."

        # Case 1: The head node itself is to be deleted
        if self.head.data == val:
            self.head = self.head.next
            return f"Deleted {val}"

        # Case 2: Search for the node
        prev = self.head
        curr = self.head.next
        while curr and curr.data != val:
            prev = curr
            curr = curr.next

        # If node not found
        if curr is None:
            return "Does not exist."

        # If found, unlink it
        prev.next = curr.next
        return f"Deleted {val}"

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")
        
    def delete2(self, val) -> str:
        if self.is_empty():
            return 'LL is empty Cant be deleted'
        
        # CASE-1: if head is to be deleted.
        if self.head.data == val:
            self.head = self.head.next
            return f'Deleted {val}'

        prev = self.head
        curr = self.head.next
        
        while curr and curr.data != val:
            prev, curr = curr, curr.next
        
        if not curr:
            return f'Node Not Found...'
        
        prev = curr.next
        return f'node Deleted {val}'
    
    
        



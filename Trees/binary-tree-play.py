class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def populate(node):
    # Ask for left child
    choice = input(f"Do you want to enter left of {node.value}? (True/False): ").strip().lower()
    if choice == "yes":
        value = int(input(f"Enter the value of the left of {node.value}: "))
        node.left = Node(value)
        populate(node.left)

    # Ask for right child
    choice = input(f"Do you want to enter right of {node.value}? (True/False): ").strip().lower()
    if choice == "yes":
        value = int(input(f"Enter the value of the right of {node.value}: "))
        node.right = Node(value)
        populate(node.right)



def display():
    display(root, "")

def display(node, indent):
    if not node:
        return

    print(indent , node.value)
    display(node.left, indent + '\t')
    display(node.right, indent + '\t')


if __name__ == "__main__":
    root_val = int(input("Enter root value: "))
    root = Node(root_val)
    populate(root)
    display(root, '\t')
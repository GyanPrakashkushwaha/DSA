

def traverse(node):
    if not node: return
    print(node.val)
    traverse(node.left)
    traverse(node.right)
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def findmin(root):
    current = root
    while current.left:
        current = current.left
    return current

def deleteNode(root, key):
    if not root:
        return root

    if key < root.data:
        root.left = deleteNode(root.left, key)

    elif key > root.data:
        root.right = deleteNode(root.right, key)

    else:
        if not root.left:
            return root.right

        if not root.right:
            return root.left

        temp = findmin(root.right)
        root.data = temp.data
        root.right = deleteNode(root.right, temp.data)
    return root

def level_order_traversal(root):
    if not root:
        return

    queue = [root]

    while queue:
        node = queue.pop(0)
        print(node.data)
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)

# Usage example: #don't mistake to balance the tree nodes either tree node will not delete.
if __name__ == '__main__':
    rootNode = TreeNode(5)
    rootNode.left = TreeNode(3)
    rootNode.right = TreeNode(8)
    rootNode.left.left = TreeNode(2)
    rootNode.left.right = TreeNode(4)
    rootNode.right.left = TreeNode(6)
    rootNode.right.right = TreeNode(10)

    # Call deleteNode on an instance of TreeNode
    rootNode = deleteNode(rootNode, 8)

    # Perform level-order traversal
    level_order_traversal(rootNode)

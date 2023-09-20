# LinkList with Queue....................

"""                      1
                       /  \
                      2    3
                     / \  / \
                    4   5 6  7

[
    [1],
    [2,3],
    [4,5,6,7],
]

"""

# class TreeNode():
#     def __init__(self,data):
#         self.data = data 
#         self.left = None 
#         self.right = None 

# rootNode = TreeNode('1') #1
# lelfChild_level_1= TreeNode('2') #2
# rightChild_level_1 = TreeNode('3') #3

# rootNode.left = lelfChild_level_1  #(1->2)
# rootNode.right = rightChild_level_1 #(1->3)

# lelfChild_level_2_L = TreeNode("4") #4
# rightChild_level_2_L = TreeNode("5") #5

# lelfChild_level_1.left = lelfChild_level_2_L #(2->4)
# lelfChild_level_1.right = rightChild_level_2_L #(2->5)

# lelfChild_level_2_L = TreeNode("6") #6
# rightChild_level_2_R = TreeNode("7") #7

# rightChild_level_1.left = lelfChild_level_2_L #(3->6)
# rightChild_level_1.right = rightChild_level_2_R #(3->7)

# print(rootNode.data)
# print(" ",rootNode.left.data)
# print(" ",rootNode.right.data)


# Perform level-order traversal--------------------------------------

# from collections import deque

# def level_order_traversal(root):
#     if not root:
#         return
    
#     queue = deque([root])

#     while queue:
#         node = queue.popleft()
#         print(node.data)
#         if node.left is not None:
#             queue.append(node.left)
#         if node.right is not None:
#             queue.append(node.right)
        

# # Call the function to perform the traversal
# level_order_traversal(rootNode)


# ------------------------------------Level Order Traversal:Best Way------------------

"""                      1
                       /  \
                      2    3
                     / \  / \
                    4   5 6  7

[
    [1],
    [2,3],
    [4,5,6,7],
]

queue = [1], nextQueue=[] , level = [1] , result = []

"""

# class TreeNode():
#     def __init__(self, data):
#         self.data = data 
#         self.left = None 
#         self.right = None 

# rootNode = TreeNode('1')
# leftChild_level_1 = TreeNode('2')
# rightChild_level_1 = TreeNode('3')
# rootNode.left = leftChild_level_1
# rootNode.right = rightChild_level_1

# leftChild_level_2_L = TreeNode('4')
# rightChild_level_2_L = TreeNode('5')
# leftChild_level_1.left = leftChild_level_2_L
# leftChild_level_1.right = rightChild_level_2_L

# leftChild_level_2_R = TreeNode('6')
# rightChild_level_2_R = TreeNode('7')
# rightChild_level_1.left = leftChild_level_2_R
# rightChild_level_1.right = rightChild_level_2_R


"""
 queue = [], nextQueue=[] , level =[]  , result = [[1],[2,3],[4,5,6,7]]
"""
def level_traversal(rootNode): #---------------------------------------------------------
    if rootNode is None:
        return []
    queue = [rootNode]
    nextQueue = []
    level = []
    result = []

    while queue != []:
        for root in queue:
            level.append(root.data)
            if root.left is not None:
                nextQueue.append(root.left)
            if root.right is not None:
                nextQueue.append(root.right)
        result.append(level)
        level = []
        queue = nextQueue
        nextQueue = []
    return result

# print(level_traversal(rootNode))

<<<<<<< HEAD
# ----------------------------------search Element in BinaryTree----------------------------------
from queue import Queue 

def SearchBinaryTree(rootNode, searchNode):
    if rootNode is None:
        return []
    queue = Queue()
    queue.put(rootNode)

    while not queue.empty():
        root = queue.get()
        if root.data == searchNode:
            print(f"{searchNode} found in the tree & the address of node is {id(root)}")
            return
        if root.left is not None:
            queue.put(root.left)
        if root.right is not None:
            queue.put(root.right)

    print("Node not found")

# SearchBinaryTree(rootNode,'3')

# ----------------------------------------insersion of binary tree-------------------------------------

"""
in binary tree >  first node is root . is node < root = leftChild . else rightChild , node > root.
"""


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert(root, data):
    if root is None:
        return TreeNode(data)  # Create a new node if the tree is empty

    if data < root.data:
        root.left = insert(root.left, data)  # Recursively insert into the left subtree
    elif data>root.data:
        root.right = insert(root.right, data)  # Recursively insert into the right subtree

    return root  # Return the updated root node

# Example usage:
rootNode = None  # Initially, an empty tree
rootNode = insert(rootNode, 5)
rootNode = insert(rootNode, 3)
rootNode = insert(rootNode, 7)
rootNode = insert(rootNode, 2)
rootNode = insert(rootNode, 4)
rootNode = insert(rootNode, 6)
rootNode = insert(rootNode, 8)
# rootNode = insert(rootNode, 9)
# rootNode = insert(rootNode, 10)
# rootNode = insert(rootNode, 11)
# rootNode = insert(rootNode, 12)

print(level_traversal(rootNode))
=======

        
    
    
>>>>>>> b08598f279f64141a449c2a007e7de0ff45cbb8c

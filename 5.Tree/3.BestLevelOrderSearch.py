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

"""

class TreeNode():
    def __init__(self, data):
        self.data = data 
        self.left = None 
        self.right = None 

rootNode = TreeNode('1')
leftChild_level_1 = TreeNode('2')
rightChild_level_1 = TreeNode('3')
rootNode.left = leftChild_level_1
rootNode.right = rightChild_level_1

leftChild_level_2_L = TreeNode('4')
rightChild_level_2_L = TreeNode('5')
leftChild_level_1.left = leftChild_level_2_L
leftChild_level_1.right = rightChild_level_2_L

leftChild_level_2_R = TreeNode('6')
rightChild_level_2_R = TreeNode('7')
rightChild_level_1.left = leftChild_level_2_R
rightChild_level_1.right = rightChild_level_2_R

def level_traversal(rootNode):
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

print(level_traversal(rootNode))

        
    
    
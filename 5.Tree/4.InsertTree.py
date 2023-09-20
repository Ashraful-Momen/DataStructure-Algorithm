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
            print(f' address => {id(root.data)} and value= {root.data}')
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


# ------------------------------------------------------PreOrderTravers-------------------------------------
def PreOrderTravers (rootNode): #root , left, right=> 
    if not rootNode: #if node is not Existence , function disclose here. (if root node exit then it has a memory address either not)
        return 
    
    print(rootNode.data) # root 
    PreOrderTravers(rootNode.left) # left recursion calling
    PreOrderTravers(rootNode.right) #right recursion calling

# ----------------------------------------insersion of binary tree-------------------------------------

"""
in binary tree >  first node is root . is node < root = leftChild . else rightChild , node > root.
"""

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        if self.data is None: 
            return TreeNode(data)

        if data < self.data:
            if self.left is None:
                self.left = TreeNode(data)  #recursively call 
            else:
                self.left.insert(data)

        elif data > self.data:
            if self.right is None:
                self.right = TreeNode(data)
            else:
                self.right.insert(data) #recursive

if __name__ == '__main__':
    print('welcome to Tree')
    rootNode = TreeNode('a')  # Initially, an empty tree
    rootNode.insert('b')
    rootNode.insert('c')
    rootNode.insert('d')
    rootNode.insert('e')
    rootNode.insert('f')
    print(level_traversal(rootNode))

    print(PreOrderTravers(rootNode))



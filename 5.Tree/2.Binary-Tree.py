# in Binary Tree , Root tree can have maximum 2 children . 
# Use : BST, Avl, Heap priority, .... 
# Full Binary Tree: root has 2 childs.
# Perfect Binary Tree : children have to same level, parent's => Left + right side need equal the edage. 
# complete : Parent nodes have to 2 childs. not need to same level / depth.
# Balance = not mandetory for parent node have to 2 childs. if parent node(without root have only 1 or 2 childs that's enough).


#Binary tree Linked List => Root -> (prev.Nodes.next) that's referens other nodes as child nodes. leafe node address/reference will be null.

# Binary tree childs: x (means)-> level , initially is x=1 (root node start from here for math easy calculation)
                    # 1.left_node => 2x 
                    # 2.right_node => 2x+1

# -------------------------create Binary Tree:--------------------------------------------
 

class TreeNode():
    def __init__(self,data):
        self.data = data 
        self.left = None 
        self.right = None 

newNode = TreeNode('Drink')

# print((newNode.data))

# ---------------------------Traversal---------------------------------------------
# pre_order = root, left, right
# post_order = left,right,root
# in_order = left, root, right

class TreeNode():
    def __init__(self,data):
        self.data = data 
        self.left = None 
        self.right = None 

newNode = TreeNode('Drink')
lelfChild = TreeNode('Cold')
rightChild = TreeNode('Hot')

newNode.left = lelfChild
newNode.right = rightChild

# print((newNode.data))

#-------------------------------------------Traversal------------------------------------------
def PreOrderTravers (rootNode): #root , left, right=> 
    if not rootNode: #if node is not Existence , function disclose here. (if root node exit then it has a memory address either not)
        return 
    
    print(rootNode.data) # root 
    PreOrderTravers(rootNode.left) # left recursion calling
    PreOrderTravers(rootNode.right) #right recursion calling


# PreOrderTravers(newNode)


def PostOrderTravers (rootNode): #left, right, root , => 
    if not rootNode: #if node is not Existence , function disclose here. (if root node exit then it has a memory address either not)
        return 
    
     
    PostOrderTravers(rootNode.left) # left , recursion calling
    PostOrderTravers(rootNode.right) #right, recursion calling
    print(rootNode.data) # root


# PostOrderTravers(newNode)

def InOrderTravers (rootNode): #left,root, right,  => 
    if not rootNode: #if node is not Existence , function disclose here. (if root node exit then it has a memory address either not)
        return 
    
     
    InOrderTravers(rootNode.left) # left , recursion calling 
    print(rootNode.data) # root
    InOrderTravers(rootNode.right) #right, recursion calling
    


# InOrderTravers(newNode)

# ==============================================Level Ways Traversal Node========================================
# traversal + point node each other  as PreOrder > root , left ,right . 
# 
# 1. print 1 level -> N1
# 2. print 2 level -> N2(left),    N3(right)
# 3. print 3 level -> [N4 (left), N5(right)], [N6(left),N7(right)].....

# ----------------------------------------------Level ways Traversal -------------------------------------------------------------------

# import QueueLinkedList  as queue  #import from QueueLinkedList.py Files


# def levelOrderTraversal(rootNode):

#     if not rootNode:
#         return 
    
#     else :
#         customQueue = queue.Queue()
#         customQueue.enqueue(rootNode)
#         while not (customQueue.isEmpty()):
#             root = customQueue.dequeue()
#             print(root.value.data) #root.value comes form QueueLinkedList file functions , (root.value).data => comes from Here Nodes Class
#             if (root.value.left) is not None:
#                 customQueue.enqueue(root.value.left)
            
#             if (root.value.right) is not None:
#                 customQueue.enqueue(root.value.right)

# ----------------------------------------------------------------

# def levelOrderTraversal(rootNode):
#     if not rootNode:
#         return 

#     customQueue = queue.Queue()
#     customQueue.enqueue(rootNode)
    
#     while not (customQueue.isEmpty()):
#         root = customQueue.dequeue()
#         print(root.value.data)

#         if root.value.left is not None:
#             customQueue.enqueue(root.value.left)
        
#         if root.value.right is not None:
#             customQueue.enqueue(root.value.right)



# -----------------------------------------------------

import QueueLinkedList  as queue  #import from QueueLinkedList.py Files

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

newBT = TreeNode("Drinks")

leftChild = TreeNode("Hot")
rightChild = TreeNode("Cold")

newBT.leftChild = leftChild
newBT.rightChild = rightChild

tea = TreeNode("Tea")
coffee = TreeNode("Coffee")

leftChild.leftChild = tea
leftChild.rightChild = coffee


def levelOrderTraversal(rootNode): #--------------------------Level ways Traversal--------------------------
    if not rootNode:
        return
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            print(root.value.data)
            if (root.value.leftChild is not None):
                customQueue.enqueue(root.value.leftChild)
            
            if (root.value.rightChild is not None):
                customQueue.enqueue(root.value.rightChild)


# levelOrderTraversal(newBT)


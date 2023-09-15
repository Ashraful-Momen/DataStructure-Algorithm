# in Binary Tree , Root tree can have maximum 2 children . 
# Use : BST, Avl, Heap priority, .... 
# Full Binary Tree: root has 2 childs.
# Perfect Binary Tree : children have to same level, parent's => Left + right side need equal the edage. 
# complete : Parent nodes have to 2 childs. not need to same level / depth.
# Balance = not mandetory for parent node have to 2 childs. if parent node(without root have only 1 or 2 childs that's enough).


#Binary tree Linked List => Root -> (prev.Nodes.next) that's referens other nodes as child nodes. leafe node address/reference will be null.

# Binary tree childs: x (means)-> level , initially is x=1 ()
                    # 1.left_node => 2x
                    # 2.right_node => 2x+1

# -------------------------create Binary Tree:--------------------------------------------
 

# class TreeNode():
#     def __init__(self,data):
#         self.data = data 
#         self.left = None 
#         self.right = None 

# newNode = TreeNode('Drink')

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

def PreOrderTravers (rootNode): #root , left, right=> 
    if not rootNode: #if node is not Existence , function disclose here. (if root node exit then it has a memory address either not)
        return 
    
    print(rootNode.data) # root 
    PreOrderTravers(rootNode.left) # left
    PreOrderTravers(rootNode.right) #right


# PreOrderTravers(newNode)


def PostOrderTravers (rootNode): #left, right, root , => 
    if not rootNode: #if node is not Existence , function disclose here. (if root node exit then it has a memory address either not)
        return 
    
     
    PostOrderTravers(rootNode.left) # left
    PostOrderTravers(rootNode.right) #right
    print(rootNode.data) # root


# PostOrderTravers(newNode)

def InOrderTravers (rootNode): #left,root, right,  => 
    if not rootNode: #if node is not Existence , function disclose here. (if root node exit then it has a memory address either not)
        return 
    
     
    InOrderTravers(rootNode.left) # left
    print(rootNode.data) # root
    InOrderTravers(rootNode.right) #right
    


InOrderTravers(newNode)


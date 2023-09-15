# root : top of the node , 
#leaf: has none of chile node 
#sibling: same parents nodes 
#Depth of nodes: root to this node of edages
#height of nodes: same of depth
#Depth of tree : depth of root node
#anestor: parent, grand-parent...previousParents of the nodes


class TreeNode():
    #add nodes
    def __init__(self, data,children=[]):
        self.data = data
        self.children = children
    
    #print space for Nodes levels
    def __str__(self,level=0):
        ret = " "*level + str(self.data)+"\n"
        for child in self.children:
            ret+=child.__str__(level+1)
        return ret 
    
    #add child
    def add_children(self,TreeNode):
        self.children.append(TreeNode)


tree = TreeNode('Drinks',[])
cold = TreeNode('cold',[])
hot = TreeNode('hot',[])

tree.add_children(cold)
tree.add_children(hot)

tea  = TreeNode('tea',[])
coffe  = TreeNode('coffe',[])
fanta  = TreeNode('fanta',[])
cola  = TreeNode('cola',[])

cold.add_children(fanta)
cold.add_children(cola)

hot.add_children(tea)
hot.add_children(coffe)

print(tree)



#bangla code : 
print('Chils of Drinks=>')
for child in tree.children:
    print(child.data)


print('Chils of Cold=>')
for child in cold.children:
    print(child.data)


print('Chils of Hot=>')
for child in hot.children:
    print(child.data)

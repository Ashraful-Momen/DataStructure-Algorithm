def add_node(vertex): #------------------------------------------
    if vertex in graph: 
        print("Node already exists") 
    else: 
        graph[vertex] = []



def add_edge(v1, v2): #------------------------------------------
    if v1 not in graph:
        print(f'{v1} does not exist in Graph')
    elif v2 not in graph: 
        print(f'{v2} does not exist in Graph')
    else: 
        graph[v1].append(v2) #a->b  
        graph[v2].append(v1) #b->a  



#for undirected and weighted graph:-----------------------------------
def add_edage_weighted(v1, v2, cost): 
    if v1 not in graph:
        print(f'{v1} is not exit in Graph')
    elif v2 not in graph: 
        print(f'{v2} is not exit in Graph')
    else: 
        # Create the weighted edge representation
        edge_v1 = [v2, cost]
        edge_v2 = [v1, cost]

        # Append the new edge to the existing list of edges for each vertex
        graph[v1].append(edge_v1) #a->b 
        graph[v2].append(edge_v2) #b->a



def delete_node_unweighted(v):  #------------------------------------------
    if v not in graph: 
        print(f'{v} does not exist in the Graph')
    else: 
        graph.pop(v) #delete node from the graph

        #now need to delete this node_item value form every graph nodes: 
        for item in graph: 
            list1 = graph[item] # list1 store nodes connected to 'item', list1 = graph[all_keys]
            if v in list1: 
                list1.remove(v) # remove list1  from every graph nodes.


def delete_node_weighted(v):#-----------------------------------------------
    if v not in graph: 
        print(f'{v} does not exist in the Graph')
    else: 
        # Remove the node from the graph
        graph.pop(v)

        # Iterate through the graph and remove any edges connected to the node
        for vertex in graph: 
            edges = graph[vertex]  # edage = [a,b,c,.....]
            for edge in edges:  # loop -> a, b, c .
                if edge[0] == v: #**** a[node,value]. we need a[node] or a[0]
                    edges.remove(edge)
                    break

def delete_edage_unweighted(v1,v2): #------------------------------
    if v1 not in graph:
        print(f"{v1} does not exit in The Graph")
    elif v2 not in graph:
        print(f"{v2} does not exit in The Graph")
    else: 
        if v2 in graph[v1]:
            graph[v1].remove(v2) # a->b , remove
            graph[v2].remove(v1) # b->a , remove

def delete_edage_weighted(v1,v2,cost): #------------------------------
    if v1 not in graph:
        print(f"{v1} does not exit in The Graph")
    elif v2 not in graph:
        print(f"{v2} does not exit in The Graph")
    else: 
        temp = [v1,cost]
        temp1 = [v2,cost]
        if temp1 in graph[v1]:
            graph[v1].remove(temp1)
            graph[v2].remove(temp)


'''
#Depth first search:
--------------------
1. Dfs = goto depth node to node then explore.
2. use stack
3. for visited node use backtrack.
'''

def dfs(graph,root): #----------------------------------------------

    if root not in graph: 
        print(f'{root} does not exit in the graph.')
        return 
      
    stack = [root] # here root is the start_node
    visited = []

    while stack : # if node exist in stack then execute lower codes.
        node = stack.pop() 

        if node in visited: # if node in visited then goto while loop level again.
            continue
        visited.append(node)

        for neighbor in graph[node]:
            stack.append(neighbor)
    
    return visited

#------------------------dfs with recursion-------------------------------------------

def dfs_recuresion(node, visited,graph):
    if node not in graph: 
        print(f'{node} does not exist in Graph')

    if node not in visited: 
        print(f'{node }') 
        visited.add(node)
        
        for i in graph[node]:
            dfs_recuresion(i,visited,graph) #recuresion here.

visited = set()
    




#------------------------end dfs with recursion---------------------------------------



graph = {}

if __name__ == '__main__': 
    add_node("A")
    add_node("B")
    add_node("C")
    add_node("D")
    add_node("E")

    add_edge("A", "B")
    add_edge("A", "C")
    
    add_edge("B", "E")
    
    add_edge("C", "D")
    
    add_edge("D", "E")
    
    
    # print("Before Delete the Graph")
    # print(graph)

    # # delete_node_unweighted("C")
    # # delete_node_unweighted("B")

    # delete_edage_unweighted("A","C")
    # print("After Delete the Graph")
    # print(graph)



    # add_edage_weighted("A", "B",50)
    # add_edage_weighted("A", "C",100)

    # print("Before Delete the Graph")
    # print(graph)

    # delete_node_weighted("C")
    # delete_node_weighted("B")

    # delete_edage_weighted("A","C",100) # if cost not match with those node then eadges not deleted.
    # print("After Delete the Graph")
    # print(graph)
    #----------------------------------dfs--------------------------
    print(graph)
    # print(dfs(graph,"A"))
    dfs_recuresion("A",visited,graph)
    print(visited)








    









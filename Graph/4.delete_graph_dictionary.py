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


graph = {}

if __name__ == '__main__': 
    add_node("A")
    add_node("B")
    add_node("C")

    add_edge("A", "B")
    add_edage_weighted("A", "C",80)
    # add_edge("B", "C")

    # delete_node_unweighted("C")
    # delete_node_unweighted("B")

    delete_node_weighted("C")

    print(graph)









# def add_node(vertex):
#     if vertex in graph: 
#         print("Node already exits") 
    
#     else: 
#         #add vertex into the graph: add in  dictionary -> graph[key]=[value]
#         graph[vertex]= []


# #for undirected and unweighted graph: 
# def add_edage(v1,v2): #-----------------------------------------------
#     if v1 not in graph:
#         print(f'{v1} is not exit in Graph')
#     elif v2 not in graph: 
#         print(f'{v2} is not exit in Graph')

#     else: 
#         graph[v1]=v2  #a->b  
#         graph[v2]=v1  #b->a



# #for undirected and weighted graph: 
# def add_edage_weighted(v1,v2,cost): #--------------------------------------------
#     if v1 not in graph:
#         print(f'{v1} is not exit in Graph')
#     elif v2 not in graph: 
#         print(f'{v2} is not exit in Graph')

#     else: 
#         list1 = [v2,cost]
#         list2 = [v1,cost]
#         graph[v1]=list1  #a->b  
#         graph[v2]=list2  #b->a


# # def delete node from graph: ---------------------------------------------
# def delete_node(v): 
#     if v not in graph: 
#         print(f'{v} not exist in the Graph')
#     else: 
#         graph.pop(v) # delete nodes from graph

#         #now need to delete this node_item value form every graph nodes: 
#         for i in graph: 
#             list1 = graph[i] # list1 store nodes connected to 'item'
#             if v in list1: 
#                 list1.remove(v)


# graph = {}

# if __name__ == '__main__': 

#     add_node("A")
#     add_node("B")
#     add_node("C")

#     # #or update this way=>    
#         # graph.update({"C":"update"})


#     add_edage("A","B")

#     # add_edage_weighted("A","C",10)

#     delete_node("A")



#     print(graph)



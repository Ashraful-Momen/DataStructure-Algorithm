def add_node(vertex):
    if vertex in graph: 
        print("Node already exits") 
    
    else: 
        #add vertex into the graph: add in  dictionary -> graph[key]=[value]
        graph[vertex]= []


#for undirected and unweighted graph: 
def add_edage(v1,v2): 
    if v1 not in graph:
        print(f'{v1} is not exit in Graph')
    elif v2 not in graph: 
        print(f'{v2} is not exit in Graph')

    else: 
        graph[v1]=v2  #a->b  
        graph[v2]=v1  #b->a



#for undirected and weighted graph: 
def add_edage_weighted(v1,v2,cost): 
    if v1 not in graph:
        print(f'{v1} is not exit in Graph')
    elif v2 not in graph: 
        print(f'{v2} is not exit in Graph')

    else: 
        list1 = [v2,cost]
        list2 = [v1,cost]
        graph[v1]=list1  #a->b  
        graph[v2]=list2  #b->a



graph = {}

add_node("A")
add_node("B")
add_node("C")

# #or update this way=>    
    # graph.update({"C":"update"})


add_edage("A","B")

add_edage_weighted("A","C",10)



print(graph)
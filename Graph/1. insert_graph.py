
#add node in grapch: 

def add_node(v): #here v is the vertex
    global nodes_count

    if v in nodes: 
        print('This node already exists!')
    
    else : 
        nodes.append(v)
        nodes_count += 1

        # add new column at last as 0 for new_node in every row:
        for n in graph:
            n.append(0)

        # add new col for new nodes: 
        tem = [] # this tem works as column

        for x in range(nodes_count): 
            tem.append(0)
        
        # now add the new col to the graph: 
        graph.append(tem)


# add edage of between 2 nodes: 
# for the directional graph=> 
    # if a->b | graph[a=row][b=col] ; 
    # if a<-b | graph[b=row][a=col] ; 

#for the undirectional grapch => 
    # if a<->b | graph[a=row][b=col]  
    #            graph[b=row][a=col] ; 

#undirected & unweighted: 
def add_edage_unweighted(vertex1,vertex2): 
    if vertex1 not in nodes: 
        print(f'{vertex1} is not exit in the nodes!')
    if vertex2 not in nodes: 
        print(f'{vertex2} is not exit in the nodes!')
    
    else : 
        #for unweighted graph: 
        # a->b , [a= row][b=col] = 1 ; [b= row][a=col] =1

        index1 = nodes.index(vertex1)
        index2 = nodes.index(vertex2)
        graph[index1][index2]=1 
        graph[index2][index1]=1

#undirected & weighted: 
def add_edage_weighted(vertex1,vertex2,cost): 
    if vertex1 not in nodes: 
        print(f'{vertex1} is not exit in the nodes!')
    if vertex2 not in nodes: 
        print(f'{vertex2} is not exit in the nodes!')
    
    else : 
        #for unweighted graph: 
        # a->b , [a= row][b=col] = 1 ; [b= row][a=col] =1

        index1 = nodes.index(vertex1)
        index2 = nodes.index(vertex2)
        graph[index1][index2]= cost
        graph[index2][index1]= cost



#print node of the graph: 
def print_graph(): 
    for i in range(nodes_count):
        for j in range(nodes_count):
            print (format(graph[i][j],"<3"),end=" ") #here "<3" use for space creating.
        print()

        pass
             

nodes = []
graph = []
nodes_count = 0

print('Before adding nodes')
print(nodes)
print(graph)

add_node("A")
add_node("B")
add_node("C")
add_node("D")

add_edage_unweighted("A","B")
add_edage_unweighted("B","D")

add_edage_weighted("A","B",10)
add_edage_weighted("B","D",10)

print('After adding nodes')
print(nodes)
print(graph)

print_graph()


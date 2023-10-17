"""
BFS(Graph, start_vertex):
    // Create a set to keep track of visited vertices
    visited = set()
    
    // Create a queue for BFS and enqueue the starting vertex
    queue = Queue()
    queue.enqueue(start_vertex)
    
    // Mark the starting vertex as visited
    visited.add(start_vertex)
    
    // While the queue is not empty
    while queue is not empty:
        // Dequeue a vertex from the queue
        current_vertex = queue.dequeue()
        
        // Process the current vertex (e.g., print it)
        process(current_vertex)
        
        // Get all adjacent vertices of the current vertex
        for neighbor in Graph.adjacent_vertices(current_vertex):
            // If neighbor is not visited, mark it as visited and enqueue it
            if neighbor not in visited:
                visited.add(neighbor)
                queue.enqueue(neighbor)

"""

from collections import defaultdict, deque

def bfs(graph, start_vertex):
    visited = set()
    queue = deque([start_vertex])
    visited.add(start_vertex)

    while queue:
        current_vertex = queue.popleft()
        print(current_vertex, end=" ")

        for neighbor in graph[current_vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# Example usage
# Create an adjacency list representing a graph
graph = defaultdict(list)
graph[0] = [1, 2]
graph[1] = [2]
graph[2] = [0, 3]
graph[3] = [3]

# Perform BFS starting from vertex 2
start_vertex = 2
print("BFS starting from vertex", start_vertex)
bfs(graph, start_vertex)


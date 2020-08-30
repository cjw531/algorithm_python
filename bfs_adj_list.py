class GraphNode:
    def __init__ (self, name):
        self.name = name # node name
        self.edges = None # adjacent node

def bfs (start):
    queue = [start]
    visited = [start]
    bfs_sequence = []

    while queue:
        node = queue.pop(0)
        bfs_sequence.append(node.name)
        
        for i in node.edges:
            if (i not in visited):
                queue.append(i)
                visited.append(i)
    
    return bfs_sequence

def bfs_adjacency_list (node):
    queue = [node]
    visited = [node] 
    adjacency_list= []
    index = 0

    while queue:
        top = queue.pop(0)
        adjacency_list.append(top)
        adjacency_list[index] = []
        
        # we don't filter by checking visited node
        for i in top.edges:
            if (i not in visited):
                queue.append(i)
                visited.append(i)
            adjacency_list[index].append(i)
        index += 1
    
    return visited, adjacency_list

if __name__ == '__main__':
    # create nodes
    A = GraphNode('A')
    B = GraphNode('B')
    C = GraphNode('C')
    D = GraphNode('D')
    E = GraphNode('E')

    # adjacent
    A.edges = [B, C, D, E]
    B.edges = [A, C]
    C.edges = [A, B, D, E]
    D.edges = [A, C]
    E.edges = [A, C]

    print("BFS graph search result:", bfs(A))
    
    print ("BFS graph adjacency list:")
    node, adj = bfs_adjacency_list(A)
    for i in range (0, len(node)):
        print (node[i].name, end=': ')
        for j in range (0, len(adj[i])):
            print (adj[i][j].name, end =' ')
        print()

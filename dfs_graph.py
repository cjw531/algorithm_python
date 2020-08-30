class GraphNode:
    def __init__ (self, value):
        self.value = value
        self.edges = None

def dfs (node, visited=None):
    if (visited == None):
        visited = []
    visited.append(node)

    for i in node.edges:
        if (i not in visited):
            dfs (i, visited)
    return visited

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

    print ("DFS graph traversal sequence:")
    dfs_result = dfs(A, None)
    for i in dfs_result:
        print (i.value, end=' ')
    print()

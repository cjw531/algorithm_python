class GraphNode:
    def __init__ (self, value):
        self.value = value
        self.edges = None

def dfs_cycle (node, visited = None, parent = None, cycle = False):
    if (visited == None):
        visited = []
    visited.append(node)

    for i in node.edges:
        if (cycle):
            return True 
        if (i not in visited):
            dfs_cycle(i, visited, node, cycle)
        elif (i in visited and parent != i):
            visited.append(node)
            cycle = True
            return True 

    return cycle

if __name__ == '__main__':
    # create nodes
    A = GraphNode('A')
    B = GraphNode('B')
    C = GraphNode('C')
    D = GraphNode('D')
    E = GraphNode('E')

    # adjacent
    A.edges = [B, C, D]
    B.edges = [A]
    C.edges = [A, D]
    D.edges = [A, B, C]
    E.edges = [D]

    print ("Test 1 graph structure:")
    print ("A-----B")
    print ("| \\")
    print ("|  \\")
    print ("|   \\")
    print ("|    \\")
    print ("C-----D-----E")

    result = dfs_cycle(A)
    print ("Graph has cycle?:", result)

    # reset adjacent
    A.edges = [B, C, D]
    B.edges = [A]
    C.edges = [A]
    D.edges = [A, B]
    E.edges = [D]

    print ("=======================")
    print ("Test 2 graph structure:")
    print ("A-----B")
    print ("| \\")
    print ("|  \\")
    print ("|   \\")
    print ("|    \\")
    print ("C     D-----E")

    result = dfs_cycle(A)
    print ("Graph has cycle?:", result)
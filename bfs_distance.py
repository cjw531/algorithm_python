class GraphNode:
    def __init__ (self, value):
        self.value = value
        self.edges = None

def bfs_distance (root):
    queue = [root]
    visited = [root]
    distance = [0]
    index = 0

    while queue:
        node = queue.pop(0)
        for i in node.edges:
            if (i not in visited):
                distance.append(distance[index] + 1)
                queue.append(i)
                visited.append(i)

        index += 1

    return visited, distance

if __name__ == '__main__':
    # initialize node
    A = GraphNode('A')
    B = GraphNode('B')
    C = GraphNode('C')
    D = GraphNode('D')
    E = GraphNode('E')

    # edges
    A.edges = [B, C, D]
    B.edges = [A, E]
    C.edges = [A, D]
    D.edges = [A, C, E]
    E.edges = [B, D]

    seq, dist = bfs_distance(A)
    for i in range (0, len(seq)):
        print ("Distance from A to", seq[i].value, ":", dist[i])
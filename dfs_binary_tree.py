class TreeNode:
    def __init__ (self, value):
        self.value = value
        self.left = None
        self.right = None

def dfs_tree (node, visited = None):
    if (visited == None):
        visited = []
    visited.append(node)

    if (node.left != None and node.left not in visited):
        dfs_tree (node.left, visited)
    if (node.right != None and node.right not in visited):
        dfs_tree (node.right, visited)

    return visited

if __name__ == '__main__':
    root = TreeNode('A')
    root.left = TreeNode('B')
    root.right = TreeNode('C')
    root.left.left = TreeNode('D')
    root.left.right = TreeNode('E')
    root.right.left = TreeNode('F')
    root.right.right = TreeNode('G')
    root.right.left.left = TreeNode('H')
    root.right.left.right = TreeNode('I')

    print("Tree Structure:")
    print ("              A")
    print ("           /     \\")
    print ("          B       C")
    print ("         /  \\    /  \\")
    print ("        D    E  F    G")
    print ("               / \\")
    print ("              H   I")

    print ("DFS tree traversal sequence:")
    result = dfs_tree (root)
    for i in result:
        print (i.value, end=' ')
    print()
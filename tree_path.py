class TreeNode:
    def __init__ (self, value):
        self.value = value
        self.left = None
        self.right = None
    
def path (root, goal, result = [], parent = None):
    if root == None:
        return []

    if (root == goal):
        result.append([root, parent])
        return result
    
    result.append([root, parent])
    path (root.left, goal, result, root)
    path (root.right, goal, result, root)
    return result

def print_path (path, root, goal):
    for i in range (len(path) - 1, -1, -1):
        if (path[i][0] == goal):
            break
        path.pop(i)

    for i in range (len(path) - 1, 0, -1):
        if (path[i][1] != path[i - 1][0]):
            path.pop(i - 1)
    
    return path

if __name__ == '__main__':
    print ("Input tree structure:")
    print ("       0")
    print ("     /   \\")
    print ("    1     2")
    print ("  /  \\")
    print (" 3    4")
    root = TreeNode(0)
    root.left = TreeNode(1)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)

    print ("Path from 0 to 4:")
    result = path(root, root.left.right)
    path = print_path(result, root, root.left.right)
    for i in path:
        print (i[0].value, end=' ')
    print()
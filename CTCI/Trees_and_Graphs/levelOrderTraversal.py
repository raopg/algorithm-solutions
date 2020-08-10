## Problem: Given a binary tree, design an algorithm that creates a list of lists, where each list contains
## all the nodes at the level.

## Solution: BFS or DFS

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def inOrderTraversalPrint(root):
    if root is None:
        return
    inOrderTraversalPrint(root.left)
    print(root.val, end=" ")
    inOrderTraversalPrint(root.right)


def levelOrderTraversal(root):
    levels = dict()

    def helper(root, level):
        nonlocal levels
        if root is None:
            return
        if level in levels:
            levels[level].append(root.val)
        else:
            levels[level] = [root.val]
        
        helper(root.left, level + 1)
        helper(root.right, level + 1)
    
    helper(root, 0)

    return list(levels.values())

if __name__ == "__main__":
    #             6
    #       5           3
    #   1       3   4       7

    root = TreeNode(6)
    root.left = TreeNode(5)
    root.right = TreeNode(3)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(7)

    print("Printing in-order first...")
    inOrderTraversalPrint(root)
    print()

    levels_lists = levelOrderTraversal(root)

    print("Level order traversal result:")
    print(levels_lists)



            
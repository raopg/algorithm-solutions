## Problem: Given a binary tree, check if it is height-balanced. A B-tree is balanced if the
## height of its left and right subtree does not differ by greater than one.


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def height(root):
    if root is None:
        return -1
    return max(height(root.left),height(root.right)) + 1

def isBalanced(root):
    if root is None:
        return True
    
    l_height = height(root.left)
    r_height = height(root.right)

    if abs(l_height - r_height) <= 1:
        return isBalanced(root.left) and isBalanced(root.right)
    
    return False

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

    print(isBalanced(root))
## Problem: Given a binary tree, determine if it is a BST
## A BST is defined as left_subtree values <= root < right_subtree values

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
def isBST(root, min_val = None, max_val = None):
    if root is None:
        return True
    
    if (min_val is not None and root.val <= min_val) or (max_val is not None and root.val > max_val):
        return False
    

    return isBST(root.left, min_val, root.val) and isBST(root.right, root.val, max_val)


if __name__ == "__main__":
    #             8
    #       5           10
    #   1      15   9       12

    root = TreeNode(6)
    root.left = TreeNode(5)
    root.right = TreeNode(10)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(15)
    root.right.left = TreeNode(9)
    root.right.right = TreeNode(12)

    print(isBST(root))
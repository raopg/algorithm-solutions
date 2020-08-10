## Problem: Given a binary tree, determine if it is a BST
## A BST is defined as left_subtree values <= root < right_subtree values

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
def isBST(root):
    if root is None:
        return True
    
    left = root.left.val if root.left else float("-inf")
    right = root.right.val if root.right else float("inf")

    return left <= root.val < right and isBST(root.left) and isBST(root.right)


if __name__ == "__main__":
    #             8
    #       5           10
    #   1      6   9       12

    root = TreeNode(6)
    root.left = TreeNode(5)
    root.right = TreeNode(10)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(9)
    root.right.right = TreeNode(12)

    print(isBST(root))
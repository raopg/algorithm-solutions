## Problem: Given a binary tree, invert its left and right subtree.
## Solution: Recursively swap the left.val, right.val down the entire tree.
## If left or right node does not exist, create one and make the other None

from tree import *

def invertTree(self, root: 'TreeNode') -> 'TreeNode':
    if root == None:
        return None
    def invertTreeRecursive(root):
        if root == None:
            return
        root.left, root.right = root.right, root.left
        invertTreeRecursive(root.left)
        invertTreeRecursive(root.right)
    
    invertTreeRecursive(root)
    return root
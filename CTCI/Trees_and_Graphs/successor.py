## Problem: Given access to a single node in a BST, find its successor.

class TreeNode:
    def __init__(self, val = 0):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None


def successor(node):
    if node is None:
        return
    
    if node.right:
        return node.right
    
    return successor(node.parent)



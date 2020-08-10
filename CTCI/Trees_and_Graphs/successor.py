## Problem: Given access to a single node in a BST, find its in-order successor.

## In-order goes => left_subtree -> root -> right_subtree
## There are a few cases here:
## 1: a node with a right subtree(right node). In this case, we want to return the leftmost child
## 2: a node with no right subtree. In this case, we are in the left subtree (possibly), 
##  and we need to get back to the parent.
class TreeNode:
    def __init__(self, val = 0):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None


def successor(node):
    if node is None:
        return None
    else:
        q = node
        x = q.parent
        while x and x.left != q:
            q = x
            x = x.parent
        return x

def leftMostChild(node):
    if node is None:
        return None
    
    while node.left:
        node = node.left
    
    return node



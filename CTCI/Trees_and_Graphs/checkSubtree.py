## Problem: Given two very large trees, find if one tree is a subtree of another.


## Solution: First find the root val in the first tree. Then recursively check if those two trees are equal

class TreeNode:
    def __init__(self, val = 0):
        self.val = val
        self.left = None
        self.right = None

def isEqual(t1, t2):
    if t1 is None and t2 is None:
        return True
    if t1 is None or t2 is None:
        return False
    
    return t1.val == t2.val and isEqual(t1.left, t2.left) and isEqual(t1.right, t2.right)

def findNode(tree, val):
    if not tree:
        return
    if tree.val == val:
        return tree
    left_search = findNode(tree.left, val)
    right_search = findNode(tree.right, val)

    return left_search if left_search else right_search


def checkSubtree(t1, t2):
    if t2 is None:
        return True
    node = findNode(t1, t2.val)

    return isEqual(node, t2)


if __name__ == "__main__":
    ## Define t1

    #           6       
    #       3       4
    #   1      5 10     7
    t1 = TreeNode(6)
    t1.left = TreeNode(3)
    t1.right = TreeNode(4)
    t1.left.left = TreeNode(1)
    t1.left.right = TreeNode(5)
    t1.right.left = TreeNode(10)
    t1.right.right = TreeNode(7)

    ## Define t2
    #      4
    #  10      7
    
    t2 = TreeNode(4)
    t2.left = TreeNode(10)
    t2.right = TreeNode(8)

    print(checkSubtree(t1, t2))




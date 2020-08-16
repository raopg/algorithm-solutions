## Problem: Given a tree and two nodes within the tree, find the lowest common ancestor of the two nodes.


## Solution: For each node in the tree, check if it is either of the two nodes. Recursively do this for every node.
## If at any point in the recursion, we have found both nodes in the left and right subtree, the
## root is LCA. We can return the root.

from tree import *

def LCA(root, p, q):
    if not root:
        return None
    ans = None
    def recurse_tree(node):
        nonlocal p,q, ans
        if not node:
            return False
        
        left = recurse_tree(node.left)
        right = recurse_tree(node.right)
        mid = node == p or node == q

        if left + right + mid >= 2:
            ans = node
        
        return mid or left or right
    
    recurse_tree(root)

    return ans

if __name__ == "__main__":
    #           6       
    #       3       4
    #   1      5 10     7
    t = TreeNode(6)
    t.left = TreeNode(3)
    t.right = TreeNode(4)
    t.left.left = TreeNode(1)
    t.left.right = TreeNode(5)
    t.right.left = TreeNode(10)
    t.right.right = TreeNode(7)

    ans = LCA(t, t.left, t.right)
    print(ans.val)
    assert ans == t

    node1 = t.left.left #1
    node2 = t.left.right #5
    expected = t.left #3
    ans = LCA(t, node1, node2)
    print(ans.val)
    assert ans == expected
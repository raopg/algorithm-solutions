## Problem: Given two nodes in a B-tree, find the first common ancestor between these nodes.
## Constraints: Solve this problem with and without a parent reference in each node.


## Solution: 
def firstCommonAncestor(self, root, p, q):
    if not root or root == p or root == q:
        return root
    
    
    left = self.lowestCommonAncestor(root.left, p, q)
    right = self.lowestCommonAncestor(root.right, p, q)
    
    # p and q appears in left and right respectively, then their ancestor is root
    if left is not None and right is not None:
        return root
    
    # p and q not in left, then it must be in right, otherwise left
    if left is None:
        return right
    
    if right is None:
        return left
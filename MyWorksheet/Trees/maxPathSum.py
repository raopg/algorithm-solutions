## Problem: Given a binary tree, find the sum of the maximum path of nodes in the tree.
## A path is considered as any sequence of nodes starting from some node along parent-child
## connections. It is not directed.

## Solution:
## Here, we want to take a recursive approach. We can define the max_value of a subtree as the max gain
## it can achieve. Max gain from a node = max(max_gain(left), max_gain(right)) + node.val

## So, we can define a function that recursively computes this max_gain for each node.
## Here is the tricky part -> we need to be able to know when the current path is the right one
## We can take the sum of this path, and compare it with a global max.



class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.maxvalue = float('-inf')
        
        def max_gain(node):
            if node is None:
                return 0
            
            left_gain = max(max_gain(node.left), 0)
            right_gain = max(max_gain(node.right), 0)
            
            price_newpath = node.val + left_gain + right_gain
            
            self.maxvalue = max(self.maxvalue, price_newpath)
            
            return node.val + max(left_gain, right_gain)
        
        max_gain(root)
        
        return self.maxvalue
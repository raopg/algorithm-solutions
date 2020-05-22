# Question: Given two trees, merge them, in such a way that ->
# 1. Return a new tree
# 2. Each node will either be a sum of two corresponding nodes if both
# exist, or the non-null node.

def mergeTrees(t1, t2):
    if t1 and t2:
        t1.val += t2.val
        t1.left, t1.right = mergeTrees(t1.left, t2.left), mergeTrees(t1.right, t2.right)
        return t1
    else:
        return t1 if t1 else t2
## Recursively add t2 to t1 nodes if they both exist. Otherwise,
## use t1 or t2 if the other is not present

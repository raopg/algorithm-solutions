## Problem: Given two trees, check whether they are the same.
## Solution: Recurse thru tree. O(N) time, constant space.

from tree import *

def sameTree(t1, t2):
    if t1 is None and t2 is None:
        return True
    if t1 is None or t2 is None:
        return False
    return t1 is t2 and sameTree(t1.left, t2.left) and sameTree(t1.right, t2.right)


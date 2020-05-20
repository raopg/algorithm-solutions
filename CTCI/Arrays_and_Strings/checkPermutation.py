# Question: Given two strings, return True if they are 
# permutations of each other.
from collections import Counter
def checkPermutation(s1, s2):
    return Counter(s1) == Counter(s2)

## Complexity analysis: O(max(m,n)) time, O(max(m,n)) space, where 
# m == len(s1) and n == len(s2)

## Can we do better? No. Even if we could sort, we still cannot avoid
# the space complexity. So, O(max(m,n)) is the best time and space complexity. 
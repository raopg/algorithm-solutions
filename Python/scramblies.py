''' The Problem: Given two strings s1 and s2, return true if characters in s1 can be rearranged to form s2.
    Ignore all punctuation.
    Two variations of this problem: 1)s1 and s2 are equal in length -> i.e, exactly n letters need to be rearranged. OR
                                    2)characters in s2 are a subset of characters in s1.
'''
from collections import Counter
def scramblies_strict(s1 : str, s2: str):
    s1 = ''.join([x for x in s1 if x.isalnum()]).lower() # O(N) - cause the loop for list comprehension runs first, then join, then lower
    s2 = ''.join([x for x in s2 if x.isalnum()]).lower()
    if len(s1) != len(s2):
        return False
    return Counter(s1) - Counter(s2) == Counter()
    

def scramblies_subset(s1 : str, s2: str):
    s1 = ''.join([x for x in s1 if x.isalnum()]).lower() # O(N) - cause the loop for list comprehension runs first, then join, then lower
    s2 = ''.join([x for x in s2 if x.isalnum()]).lower()
    
    c1 = Counter(s1)
    c2 = Counter(s2)

    for c,freq in c2.items():
        if c not in c1:
            return False
        elif c2[c] != freq:
            return False
        
    return True


print(scramblies_subset('abc', 'abc'))



## Problem: Given two strings, return True if one is an anagram of the other.

## Solution: Use hashset Counter for counting freq of chars.

## Time Complexity: O(N), Space complexity: O(N). We cannot do better.

from collections import Counter
def valid_anagram(s1, s2):
    c = Counter(s1)
    for char in s2:
        if char not in c:
            return False
        c[char] -= 1
        if c[char] == 0:
            del c[char]
    return c == {}
    

## one-liner, better time(slightly due to inbuilt Python)
## But O(len(s1) + len(s2)) space

def valid_anagram_one_liner(s1, s2):
    return Counter(s1) == Counter(s2)
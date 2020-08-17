## Problem: Given a list of strings, return a list of lists, where each list contains all
## strings which are anagrams of each other.


## Solution: We need to convert our frequency into something hashable.
## We know that the common aspect of anagrams are their freq dicts.
## We can convert this into an encoded tuple that is hashable.
## How do we maintain order? We can sort the strings, OR, generate the tuple based on 
## alphabetical order.

## Approach -> for each string in the list, create a tuple of size 26 where
## each position corresponds to the freq of chr(i) + 'a'.
from collections import defaultdict
def groupAnagrams(strs):
    ret = defaultdict(list)
    for s in strs:
        count = [0] * 26

        for char in s:
            count[ord(char) - ord('a')] += 1
        
        ret[tuple(count)].append(s)
    
    return ret.values()

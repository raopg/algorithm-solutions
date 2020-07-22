## Question: Given two strings, write a function to check if they are one edit or zero edits away from each other
## An edit is defined as one of three operations:
## 1. Insert a character
## 2. Delete a character
## 3. Replace a character

## Solution:
## The idea is to iteratively check thru both strings. We can determine beforehand whether a replacement
## is required or an insertion is required by checking the lengths of both strings.
## We also need to keep track of which string is longer and which is shorter because we need to only advance pointers
## of the longer string when we actually do insertion/ shorter string when we do deletion

## Time and Space Complexity Analysis:
## Time: O(N)
## Space: O(N) // But this is mainly because we need to determine shorter and longer strings.

def oneAway(str1, str2):
    longer, shorter = (str1, str2) if len(str1) > len(str2) else (str2, str1)
    edited = False

    shorter_idx = 0
    longer_idx = 0

    while shorter_idx < len(shorter) and longer_idx < len(longer):
        if longer[longer_idx] != shorter[shorter_idx]:
            if edited:
                return False
            edited = True

            if len(shorter) == len(longer):
                shorter_idx += 1
        else:
            shorter_idx += 1
        longer_idx += 1
    
    return True

# print(oneAway('pale', 'ple'))
# print(oneAway('ple', 'bale'))

# Question: Given a string, implement an algorithm to 
# check if it has unique characters.

def isUnique(string):
    if string == '' or len(string) == 1:
        return True
    freq = dict()
    for char in string:
        if char in freq:
            return False
        freq[char] = 1
    return True
# print(isUnique('aaaab'))
# print(isUnique('adcxsaer'))
# print(isUnique('a'))

## Time Complexity Analysis: O(n) time, O(n) space.

## Can we do it in O(1) space? Bit manipulation!

def isUniqueSpaceOptimized(string):
    bit = 0

    for i in range(len(string)):
        ascii_val = ord(string[i]) - ord('a')

        if bit & (1 >> ascii_val):
            return False
        
        bit |= (1 >> ascii_val)
    return True

# print(isUniqueSpaceOptimized('abcd'))
# print(isUniqueSpaceOptimized('asasasaaaa'))
# print(isUniqueSpaceOptimized(''))
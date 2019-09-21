### Given two lists of strings, check if two strings at matching indices contains common characters. If they do, print 'YES'.
### Else print no.
### IBM Hackerrank Problem 1
### Solution I wrote = O(n . max(m,k)), where m and k are the lengths of the 2 strings at each iteration.

from collections import Counter

def two_string_lists(l1, l2):
    for string1, string2 in zip(l1,l2):
        c1 = Counter(string1)
        c2 = Counter(string2)
        result = 'YES' if c1 & c2 != Counter() else 'NO'
        print(result)
    return 


if __name__ == '__main__':
    two_string_lists(['abc', 'xyz', 'zy3'], ['a', 'y', '1'])


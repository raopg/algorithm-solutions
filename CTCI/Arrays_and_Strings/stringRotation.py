## Problem: Assume you have a method isSubstring which checks if one word is a substring
## of another. Given 2 strings s1, s2, write code to check if s2 is a rotation of s1
## using only one call to isSubstring.

## Solution: The solution is simple, because, s1 is cut into 2 parts in order to make s2.
## So, if we add s1 to itself, and compare if s2 is a substring to s1s1, we are done!

def isRotation(s1, s2) -> bool:
    
    if len(s1) != len(s2) or len(s1) == 0:
        return False

    return isSubstring(s1+s1, s2)
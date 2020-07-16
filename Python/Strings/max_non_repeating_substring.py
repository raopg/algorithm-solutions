"""
    Problem: Given a string, find the length of the largest substring
    with no duplicates.

    Example: abcabcabb
    Answer: 3

    Example: aaaaaaaa
    Answer: 1

    Problem Number: LC 3
"""
"""
    Solution:
    Core Concepts: Strings, Sliding Window, HashSet/HashMap

    The idea is, for each letter we need to check if it is repeated
    in the current substring. If so, we can simply SLIDE the window
    i.e our substring to the last occurence of the letter and move on.
    We also maintain a max value, representing the length of the largest
    non-repeating substring we have seen so far.
"""
## Code:

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = len(s)
        start = 0
        max_length = 0
        seen = dict()
        # abcabcbb
        for i in range(length):
            if s[i] not in seen: #b seen = {a:0, b:1, c:3}
                seen[s[i]] = i
                if (i - start + 1 > max_length): # 3 > 0
                    max_length = i - start + 1 # 3
            else:
                index = seen[s[i]]
                
                for char in s[start : index]:
                    del seen[char]
                seen[s[i]] = i
                
                start = index + 1
        return max_length
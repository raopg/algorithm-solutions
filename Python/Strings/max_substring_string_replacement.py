"""
    Problem: Given a string that contains only uppercase letters,
    you are allowed to perform k operations on the string, where each
    operation is defined as changing a character in the string to any
    other uppercase character.

    Find the max length of the substring that contains all repeeating
    characters that you can obtain by performing k operations.

    Example: ABAB, k = 2
    Output: 4
    You can change A's or B's to get AAAA or BBBB

    Exmaple: ABAAABABB k = 1
    Output: 5
    You can change B at index 1 or index 5 to A to get the answer.
"""
"""
    Solution: 
    We can apply the sliding window approach to this problem.
    In each window, we can check if the number of characters
    is greater than the sum of k and the number of most repeated 
    character. If true, we resize the window till we achieve a
    substring which satisfies the constraint given. We can maintain
    a max length, to determine the longest such substring.
"""

## Code:
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start = 0
        window = {}
        max_count = 0
        max_length = 0
        
        
        for end in range(len(s)):
            if s[end] not in window:
                window[s[end]] = 0
            
            window[s[end]] += 1
            max_count = max(max_count, window[s[end]])
            
            while end - start - max_count + 1 > k:
                start_char = s[start]
                start += 1
                
                window[start_char] -= 1
                if window[start_char] == 0:
                    del window[start_char]
                
            max_length = max(max_count, end - start + 1)
        
        return max_length

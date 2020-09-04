## Problem: Given a string, find the maximum substring that does not contain any repeating characters.
## Solution: Sliding window, maintain a dict of values mapping them to last seen indices.
## If we have seen the value before, remove all values from current window start to the last occuring
## index of the repeated char

def maxSubstring(s):

    window_start = 0
    max_sum = 0
    last_index = dict()
    for window_end in range(len(s)):
        curr_char = s[window_end]

        if curr_char not in last_index:
            last_index[curr_char] = window_end
        else:
            idx = last_index[curr_char]
            for c in s[window_start:idx]:
                del last_index[c]
            window_start = window_end
        max_sum = max(max_sum, window_end - window_start + 1)
    return max_sum

if __name__ == "__main__":
    assert maxSubstring('acbcasa') == 3
    assert maxSubstring('bbbbbbbbb') == 1
    print(maxSubstring('aaaaaaaaab'))
        

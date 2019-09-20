#### Problem Statement: Given two strings, find the longest common subsequence among them. ####
#### LCS => Longest string that is common among two strings ####
#### Two variations of this problem: 1) Find the length of the LCS
####                                 2) Find the LCS itself.

def length_solution(x: str, y: str):
    if len(x) == 0 or len(y) == 0:
        return 0
    if x[0] == y[0]:
        return 1 + length_solution(x[1:], y[1:])
    else:
        return max(length_solution(x[1:], y), length_solution(x,y[1:]))
    
def string_solution_recursive(x: str, y: str):
    if len(x) == 0 or len(y) == 0:
        return []
    if x[0] == y[0]:
        return list(x[0]) + string_solution_recursive(x[1:], y[1:])
    else:
        lcs1 = string_solution_recursive(x, y[1:])
        lcs2 = string_solution_recursive(x[1:], y)
        return lcs1 if len(lcs1) > len(lcs2) else lcs2
    
def string_solution(x: str, y: str):
    lcs_list = string_solution_recursive(x,y)

    return ''.join(lcs_list)


if __name__ == "__main__":
    assert string_solution("abcdef", "abc") == "abc"
    assert length_solution("abcdef", "abc") == 3


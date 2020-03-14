def solution(str):
    freq = set()
    for c in str:
        if c in freq:
            return c
        freq.add(c)
    return None

print(solution('abcda'))
''' The Problem: Given a list of integers, return the values and positions of local maxima and plateaus.
    Maxima: Prev value < Maximum > Next Value
    Plateau: Prev value< Plateau == Plateau .... > Next lower value

    Input: A list L containing the integers.
    Output: A dictionary containing two lists: a "pos" list for the index positions, and "peaks" list. For an empty list, return {"pos": [], "peaks": []}
'''


def solution( L:[int] ):
    pos, picks = [], []
    picks_info = {"pos": [], "picks": []}

    if not len(L):
        return picks_info

    for i in range(1, len(L)):
        if L[i] > L[i-1]:
            pos = [i]
            picks = [L[i]]
        
        elif L < L[i-1]:
            picks_info['pos'].extend(pos)
            picks_info['picks'].extend(picks)
            pos, picks = [], []
    return picks_info
    
## Problem: Given a matrix of characters and a target word, design an algorithm to 
## check if the word can be constructed from the matrix.
## Rules for construction: Any word can be constructed by sequentially adding together characters
## that occur adjacent to each other.

## Solution: We can perform a DFS from each position in the matrix to see if the characters
## occur sequentially in a DFS search. However, we need to backtrack in the event we dont find the
## word we are looking for. We need to backtrack at each "level" of the DFS.

## Time Complexity : O(N.3^L) where L is the length of the word.
## How? In each recursive DFS call, we explore 3 nodes(ignore the original, visited node)
## This gives us a call stack of 3-ary tree, where the height is L(the number of characters in the search word)

## Space Complexity: O(L) -> we make 3*L recursive calls.

def exist( board: List[List[str]], word: str) -> bool:
        
    if not board and not word:
        return True
    if not board:
        return False
    
    M = len(board)
    N = len(board[0])
    
    def backtrack(row, col, remaining_word):
        nonlocal board, M,N
        if len(remaining_word) == 0:
            return True
        
        ## If search box is invalid, return False
        if row < 0 or row == M or col < 0 or col == N:
            return False
        
        ## If remaining word does not start with current box's val, return False
        if board[row][col] != remaining_word[0]:
            return False
        
        ## Set the current box to visited
        board[row][col] = "*"
        directions = [(-1,0), (0,1), (1,0), (0,-1)]
        
        ## For each direction, perform DFS and backtrack with result.
        for row_dir, col_dir in directions:
            if backtrack(row + row_dir, col + col_dir, remaining_word[1:]):
                return True
        ## If the search was unsuccessful, mark the node unvisited for other searches.
        board[row][col] = remaining_word[0]
        
        return False
    
    
    for i in range(M):
        for j in range(N):
            if backtrack(i, j, word):
                return True
    
    return False

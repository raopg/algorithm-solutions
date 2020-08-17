## Problem: Given a matrix of characters and a list of words, return all the words that can be 
## constructed from the matrix.

## Similar to Word Search I, construction is defined as sequentially building a word by taking 
## vertically and horizontally adjacent characters.

## Solution: We can implement a recursive DFS with backtracking, similar to word search I.
## But to store the list of words, we can use a trie structure and its contains method.
## At each recursive level, we can check if the prefix we have so far exists within the trie.
## Further, we can check if the word in the trie ends there. If so, append it to a return array.

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        WORD_END = '#'
        
        trie = {}
        
        for word in words:
            node = trie
            for letter in word:
                node = node.setdefault(letter, {})
            
            node[WORD_END] = word
        
        M = len(board)
        N = len(board[0])
        
        ret = []
        
        def backtracking(row, col, parent):
            nonlocal board, ret, M, N
            
            letter = board[row][col]
            curr = parent[letter]
            
            word_match = curr.pop(WORD_END, False)
            
            if word_match:
                ret.append(word_match)
            
            board[row][col] = "*"
            
            directions = [(-1,0), (1,0), (0,-1), (0,1)]
            
            for row_dir, col_dir in directions:
                next_row, next_col = row + row_dir, col + col_dir
                
                if next_row < 0 or next_row >= M or next_col < 0 or next_col >= N:
                    continue
                if board[next_row][next_col] in curr:
                    backtracking(next_row, next_col, curr)
            board[row][col] = letter
            
            
            if not curr:
                parent.pop(letter)
        
        for i in range(M):
            for j in range(N):
                if board[i][j] in trie:
                    backtracking(i, j, trie)
        
        
        return ret
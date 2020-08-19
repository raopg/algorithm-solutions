## Problem: Given a 2-D matrix, containing 1's and 0's, where 1 represents land
## and 0 represents water, find the number of islands in the matrix.

## Solution: Here, we can employ a DFS/BFS solution on the matrix.
## General idea: For every 1, explore all neighboring nodes that are 1.
## We want to discard all these connected 1's because they belong to the same
## island. Keep doing this for every value in the matrix.

## Discarding/invalidating connected 1's: There are two ideas here.
## We can make all connected 1's (except the one we just encountered) to 0,
## thereby "minimizing" the area of the array to 1 -> the number of island.
## This will mutate the original matrix.
## An alternate approach, which requires more space, is to store all visited 1's
## in a set. So, if it is in visited, it's not a new island. So no need to explore.
## Second approach is more desirable if we want to keep the original matrix for reference
## or future use. Either way, 90% of the solution is the same for both ideas.

## Pseudocode:
## Null check matrix
## Get matrix dimensions
## Initialize count to 0
## For each row in matrix:
##      For each col in matrix:
##          if matrix(row, col) == 1 and matrix not in visited_set
##              DFS(row, col)
##              count += 1
## DFS(row, col)
##      Check if row, col is valid in matrix
##      Check if row, col is 0. If it is, return because we are done
##      For each direction in [up, down,left, right]
##          DFS(row,col + direction)

def numIslands(matrix):
    M = len(matrix)
    if M == 0:
        return 0
    N = len(matrix[0])

    count = 0 ## This is what we return
    visited = set()
    def is_valid(x,y):
        if x < 0 or x == M or y < 0 or y == N:
            return False
        return True
    def dfs(x, y):
        if not is_valid(x,y) or matrix[x][y] == '0':
            return
        directions = [(0,1), (1,0), (0,-1), (-1,0)]

        for row_delt, col_delt in directions:
            dfs(row_delt+x, col_delt+y)

    for x in range(M):
        for y in range(N):
            if matrix[x][y] == '1' and (x,y) not in visited:
                dfs(x,y)
                count += 1

    return count

## Time Complexity: O(M.N) -> We have 2 nested loops.
## Space Complexity: O(M.N) -> At worst (matrix is all 1's), we get a recursive call stack 
## for DFS of size M.N



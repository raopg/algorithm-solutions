## Problem: There is a MxN grid that contains some oranges. The orange can be either rotten or fresh
## After each minute (can be any fixed interval of time), all the fresh oranges next to a rotten orange 
## become rotten. Return the min. time that must elapse after which all oranges are rotten.
## If all of them cannot rot, then return -1.

## Solution: Here we can use BFS to search for all adjacent cells of rotten oranges. If there is a fresh orange,
## we increment the time, decrement the fresh orange count and set it to rotten.
## We repeat till the BFS queue is empty. 
## Before BFS, we can compute the number of fresh oranges, and append all rotten oranges to the BFS queue.
## We can determine if all oranges are rotten if the number of fresh oranges is 0 at the end of our BFS search.

## Time, Space Complexity := O(M.N) time, O(M.N) space (worst-case)

from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        
        fresh_oranges = 0
        R, C = len(grid), len(grid[0])
        
        ## Here we want to add all rotten oranges to the q, and count number
        ## of good oranges.
        for row in range(R):
            for col in range(C):
                if grid[row][col] == 2:
                    queue.append((row,col))
                elif grid[row][col] == 1:
                    fresh_oranges += 1
        
        
        queue.append((-1,-1))
        
        minutes_elapsed = -1
        
        directions = [(-1,0), (0,1), (1,0), (0,-1)]
        
        while queue:
            row, col = queue.popleft()
            
            if row == -1:
                minutes_elapsed += 1
                if queue:
                    queue.append((-1,-1))
            else:
                ## For each neighbor
                for d in directions:
                    ## Find the neighbor
                    neighbor_row, neighbor_col = row + d[0], col + d[1]
                    
                    ##Check if neighbor is a valid cell in grid
                    if R > neighbor_row >=0 and C > neighbor_col >= 0:
                        ## Check if neighbor has a fresh orange
                        if grid[neighbor_row][neighbor_col] == 1:
                            ## Set it to rotten
                            grid[neighbor_row][neighbor_col] = 2
                            ## Reduce the number of fresh oranges
                            fresh_oranges -= 1
                            
                            ## Add this to the q of rotten oranges, because it is now rotten.
                            queue.append((neighbor_row, neighbor_col))
                            
        ## If # of fresh_oranges != 0, then there must be a fresh orange in the grid that is not next to a rotten orange( or a rotting one)
        return minutes_elapsed if fresh_oranges == 0 else -1
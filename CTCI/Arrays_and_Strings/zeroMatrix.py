## Problem: Write an algorithm such that if an element in an MxN is 0, its entire row and column is set to 0.

## Solution: 
## First idea is to simply iterative through matrix and capture all rows and columns that are needed to be 0
## Then perform a second iteration and keep checking if i or j is in the set of rows/cols that needed to be made 0.
## Time and Space Complexity : O(M.N), O(k) where k = # of zeroes in matrix
def zeroMatrixNaive(matrix):
    row_zeroes = set()
    col_zeroes = set()

    m,n = len(matrix), len(matrix[0])

    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                row_zeroes.add(i)
                row_zeroes.add(j)
    
    for i in range(m):
        for j in range(n):
            if i in row_zeroes or j in col_zeroes:
                matrix[i][j] = 0
    
    return matrix

## We can improve this solution further by setting the first elem in row and col to 0 whenever we do find
## a zero in that row and col.

def zeroMatrix(matrix):
    m,n = len(matrix), len(matrix[0])


    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0
            elif matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0
    for i in range(m):
        for j in range(n):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j]
    
    return matrix

## The second solution has O(1) space. 
            
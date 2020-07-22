## Problem: Given an image representted by an NxN matrix, where each pixel in the image is 4 bytes,
## write a method to rotate the image by 90 degrees. Can you do this in-place?
## Can you write a generalized algorithm for any degree rotation that is mod 90?

## Solution: We need to swap all elements from top, right, left and bottom for each layer in the square matrix
## We can do this by swapping like so:
# temp = top[i]
# top[i] = left[i]
# left[i] = bottom[i]
# bottom[i] = right[i]
# right[i] = temp


def rotateMatrix(mat):
    n = len(mat)

    if n == 0 or n != len(mat[0]):
        return False
    
    for layer in range(n//2):
        start = layer
        end = n - layer - 1

        for i in range(start, end):
            offset = i - start
            top = mat[start][i]

            mat[start][i] = mat[end-offset][start]

            mat[end-offset][start] = mat[end][end-offset]

            mat[end][end-offset] = mat[i][start]

            mat[i][end] = top
    return True
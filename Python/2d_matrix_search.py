# Question: Given a SORTED 2D matrix and a search key, 
# find out if it exists in the matrix

## Obviously we can do this trivially in O(M * N) time and O(1) space
## Can we do better? Yeah! With binary_search

class Solution:
    def bin_search(self, lst, val, l, r):
        if r < l:
            return False   
        mid = l + (r - l) // 2
        
        if lst[mid] == val:
            return True
        elif lst[mid] <= val:
            return self.bin_search(lst, val, mid+1, r)
        else:
            return self.bin_search(lst, val, l, mid -1)
            
        
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for lst in matrix:
            if self.bin_search(lst, target, 0, len(lst) - 1):
                return True
        return False

### Getting index of the key should  be 
# trivial from the above the solution above. We can just iterate
# using row number and find the col number in binary_search.

## Dead giveaway of bin_search -> sorted array

## But since the whole thing is sorted, we can reduce the row 
# iteration to log M time. Skipping bin_search code here.

def searchMatrixBinary(matrix, target):
    for arr in matrix:
        if not len(arr):
            continue
        if arr[-1] > target:
            continue
        elif arr[0] > target:
            return False
        elif arr[0] <= target and arr[-1] >= target:
            return binary_search(arr, 0, len(arr) - 1)
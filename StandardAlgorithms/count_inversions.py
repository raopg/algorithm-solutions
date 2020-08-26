## Problem: Given an input array, find the total number of inversions in the array.
## An inversion is defined a pair (i,j) where i < j and arr[i] > arr[j] (or arr[i] >= arr[j], depends on use case)

## Solution: We can modify the merge sort. The intuition is like so -
## Since in merge sort, we have a left subarray and a right subarray,
## the first condition for count inversions are met when we try to merge these elements(i < j)
## If, at any point in the merge step, we choose an element from the right subarray
## BEFORE all left subarray elements are written into the array, then the number of
## remaining elements in the left subarray are the inversions.

## Ex: [1,3,5,2,4,6] => [1,3,5] and [2,4,6]
## Merging => [1, 2, 3, 4, 5, 6]
##                      ^ we have i = 2, len(L) - i = 1 elements    
##                ^ we have i = 1, len(L) - i = 2 elements that are remaining, but we use right subarray.
## Total inversions: 2 + 1 = 3 == [(3,2), (5,2), (5,4)]


def count_inversions(arr):
    if len(arr) <= 1:
        return 0
    else:
        mid = len(arr) // 2
        
        ##Split into two subarrays
        L = arr[:mid]
        R = arr[mid:]

        left_count = count_inversions(L)
        right_count = count_inversions(R)

        ## Merge step
        i = j = k = 0
        inversions = 0
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                ## Count inversions
                inversions += len(L) - i
                arr[k] = R[j]
                j += 1
            k += 1
        
        while i < len(L):
            inversions += 1 ## Leftover inversions
            arr[k] = L[i]
            i += 1
            k += 1
        
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
        return inversions

if __name__ == "__main__":
    arr = [1,3,5,2,4,6]
    inv = count_inversions(arr)

    print(inv, arr)

## Problem: Standard sorting.

## Advantages of quicksort:
## 1. One of the greatest algorithms every construed.
## 2. Does not use additional memory (unlike merge sort)
## 3. Elegant

## Key Ideas:
## Partition the array around a pivot element.
## Rearrange array such that all elements that come before pivot are less than pivot and similarly for elements
## that come after the pivot.
## This is partial, because we dont necessarily get the order right amongst left and right elements
## One this is for certain, the pivot element is in its rightful place.

## Partionting facts:
## O(N) time, O(1) space, fast for sorting algorithms
## Enables a D/C approach. After partitioning, we recursively sort elements on left and right of pivot.

## Pseudocode:
## QuickSort(A, n):
##  if n == 1: Return
##  p = ChoosePivot(n)
##  Partition A around p
##  QuickSort(A[1...p], p)
##  QuickSort(A[p+1...n], n-p)

## Partitioning A around p:
## Swap the pivot with the first element (O(1)) preprocessing

def partition(A, left, right):
    pivot = A[left]
    i = left + 1

    for j in range(left + 1, right):
        if A[j] < pivot:
            A[j], A[i] = A[i], A[j]
            i += 1
        j += 1
    
    A[left], A[i-1] = A[i-1], A[left]

    return i-1

def quick_sort(A, left, right):
    if not A or len(A) == 1:
        return
    ## Choose pivot
    if left < right:
        pivot = partition(A, left, right)

        quick_sort(A, left, pivot - 1)
        quick_sort(A, pivot + 1, right)


if __name__ == "__main__":
    ## Test partition
    A = [2,8,5,1,4,7,6,3]
    # partition(A, 0, len(A))
    # print(A)

    quick_sort(A, 0, len(A))
    print(A)
        
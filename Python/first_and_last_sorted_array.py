## Problem: Given a sorted array and target value, find the first and last occurence(index) of the element

## Solution1 : Binary search. Once you find the target, loop backwards and forwards to find the
## first and last occurence. Return that pair of indices.

def find_first_last(arr, key):
    l = 0 
    r = len(arr) - 1

    while l <= r:
        mid = l + (r - l) // 2

        if arr[mid] == key:
            found_l = found_r = mid

            while found_l > 0 and arr[found_l - 1] == key:
                found_l -= 1
            while found_r < len(arr) - 1 and arr[found_r + 1] == key:
                found_r += 1
            
            return (found_l, found_r)
        elif arr[mid] < key:
            l = mid + 1
        else:
            r = mid - 1
    
    return (-1,-1)

## The above solution is suboptimal because it can devolve into an O(n) algorithm (Ex: If the entire array)
## consisted of only the target.

## Here is a optimized approach:
## We use binary search for two purposes, and we can denote which purpose using a boolean flag.
## If the flag is true, we find the leftmost occurrence of the key using binary search
## Else, we find the rightmost occurence of the key using binary search.
## In our main function, we run this search once to find the leftmost occurence. If we cant find
## anything, we immediately return -1,-1
## Else, we return the left bound, and the right bound (which we get after calling binary search with flag = False)

def binary_search_extreme(arr, target, left):
    bound = None
    l = 0
    r = len(arr) - 1

    while l <= r:
        mid = l + (r - l) // 2

        if left:
            if arr[mid] >= target:
                r = mid - 1
            else:
                l = mid + 1
        else:
            if arr[mid] <= target:
                l = mid + 1
            else:
                r = mid - 1
        if arr[mid] == target:
            bound = mid
    
    return bound if bound else -1

def search(arr, target):
    left_bound = binary_search_extreme(arr, target, True)

    if left_bound == -1:
        return [-1, -1]
    
    return [left_bound, binary_search_extreme(arr, target, False)]

if __name__ == "__main__":
    arr = [2,3,6,7,7,8,8,8,12]

    for i, val in enumerate(arr):
        print(i,':', val, end = "  ")

    # print(find_first_last(arr, 8))
    # print(find_first_last(arr, 7))

    print()
    print(search(arr, 8))
    print(search(arr, 7))
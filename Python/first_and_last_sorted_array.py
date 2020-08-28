## Problem: Given a sorted array and target value, find the first and last occurence(index) of the element

## Solution: Binary search. Once you find the target, loop backwards and forwards to find the
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


if __name__ == "__main__":
    arr = [2,3,6,7,7,8,8,8,12]

    for i, val in enumerate(arr):
        print(i,':', val, end = "  ")

    print(find_first_last(arr, 8))
    print(find_first_last(arr, 7))
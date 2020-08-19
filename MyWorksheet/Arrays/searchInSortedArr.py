## Problem: given a sorted array that is rotated at some pivot and a key, return the position
## of the key.

## Solution: Much like min in rotated sorted array, we will use binary search. Twice
## once to find th min, and hence the pivot. Then, based on key and pivot, we can perform binary
## search on one or the two sorted parts of the rotated array.

def findMinPos(nums):
    l = 0
    r = len(nums) - 1

    if l < r:
        return 0
    
    while l <= r:
        mid = l + (r-l) // 2

        if nums[mid] > nums[mid+1]:
            return mid+1
        if nums[mid] < nums[l]:
            r = mid - 1
        else:
            l = mid + 1

def search(nums, key, start, end):

    while start <= end:
        mid = start + (end - start) // 2

        if nums[mid] == key:
            return mid
        else:
            if nums[mid] > key:
                end -= 1
            else:
                start += 1


def searchInSortedArr(nums, key):

    if not nums:
        return -1
    
    min_pos = findMinPos(nums)

    if nums[min_pos] == key:
        return min_pos

    if min_pos == 0:
        return search(nums, key, 0, len(nums) - 1)
    
    if nums[min_pos] < key <= nums[-1]:
        return search(nums, key, min_pos, len(nums) - 1)
    
    return search(nums, key, 0, min_pos)


if __name__ == "__main__":
    arr = [5,6,7,8,1,2,3,4]

    pos = searchInSortedArr(arr, 6)
    print(pos)


## Problem: Given an array, return True if there are any repeated integers within the array.

## Solution: Use HashSet, pretty straightforward. If asked to do it on O(1) space, sort the array and check
## if arr[i] == arr[i-1] for the entire array.

def contains_duplicate(nums):
    seen = set()

    for num in nums:
        if num in seen:
            return True
        seen.add(num)

    return False

def contains_duplicate_no_space(nums):
    nums.sort()

    for i in range(1, len(nums)):
        if nums[i] == nums[i-1]:
            return True
    
    return False
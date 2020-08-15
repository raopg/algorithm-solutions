## Problem: Given a list of numbers and a target, find a pair of numbers within the list that
## add up to the target.

## Solution: We can use a hashset the contains all elements that we have seen so far.
## For each element in the array, we can check if the target - curr_elem is in the list.

def twoSum(nums, target):
    seen = set()

    for num in nums:
        if target - num in seen:
            return [num, target - num]
    
        seen.add(num)

## Time Complexity: O(N) average/worst
## Space Complexity: O(N) average/worst
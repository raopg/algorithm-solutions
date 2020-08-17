## Problem: Given a list of numbers, return the max product of any of its sublists.

## Solution: Kadane DP algorithm, same for maxSubarray DOES not work here, because two negatives can 
## result in a bigger sized subarray. We need to modify our DP approach like so:

## There are two types of values that can cause problems -> negatives and zeroes
## For negatives, we can keep both a min and max, so that the min will contain a value that has been
## multiplied with a negative, but will be "saved" if we encounter another negative.
## For zeroes, we can store the highest result we have seen so that we return that if we encounter
## a zero later in the array.


def maxProductSubarray(nums):

    if not nums:
        return 0

    max_val = nums[0]
    min_val = nums[0]
    result = max_val

    for i in range(1, len(nums)):
        curr_val = nums[i]

        curr_max = max_val
        max_val = max(curr_val, curr_max * curr_val, min_val * curr_val)
        min_val = min(curr_val, curr_max * curr_val, min_val * curr_val)

        result = max(max_val, result)
    
    return result
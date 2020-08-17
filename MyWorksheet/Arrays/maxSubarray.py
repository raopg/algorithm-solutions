## Problem: Given an array of integers, return the max_sum of a subarray of that array.
## Ex: [2,5,20,-7] => 27(2,5,20), [-1,0,1,1,-2] => 2(1,1 or 0,1,1)

def maxSubarray(nums):
   curr_sum = max_sum = nums[0]

    for i in range(1, len(nums)):
       curr_sum = max(nums[i], curr_sum + nums[i])
       max_sum = max(max_sum, curr_sum)
    
    return max_sum


## We can also approach this using Kadane's Algorithm, which is a DP approach.
## Essentially, we repurpose nums to store max_sum we have seen so far.
def maxSubarrayDP(nums):
    if len(nums) == 1:
        return nums[0]
    
    for i in range(1, len(nums)):
        nums[i] = max(nums[i], nums[i-1] + nums[i])
    
    return max(nums)

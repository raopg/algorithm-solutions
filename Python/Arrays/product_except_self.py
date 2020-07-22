"""
    Problem: Given an array of numbers called nums, return an array 'output' such that
    output[i] is equal to the product of all numbers in nums, except nums[i]

    You cannot use division. Expected space and time complexityL O(n)
"""
"""
    Solution: The basic idea here is that each output[i] can be written as product output[:i] 
    multiplied by product of output[i:]

    We can use supplemental arrays to denote this left product and right product, but that is
    not optimal space-wise. Solution - make two O(n) passes. The first is computing left product in output array,
    the second is computing right product. By using proper indices, we can "miss" 
    each value in the product calculation
"""
## Code:

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        result = [1] * length

        for i in range(1, length):
            result[i] = result[i-1] * nums[i-1]

        R = 1
        for i in reversed(range(length)):
            result[i] = result[i] * R
            R *= nums[i]

        return result
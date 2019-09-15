''' Given an integer array, find the continuous subarray that has the largest sum. Return the sum
    Time complexity: O(n)
'''

def max_subarray(nums: List[int]):
    '''The basic idea is to compute the max subarray for each index place. If the next element increases the value of that subarray, then that is the new best sum.
    '''
    if len(nums) == 1:
        return nums[0]
    for i in range(1,len(nums)):
        nums[i] = max(nums[i], nums[i] + nums[i-1]) # Repurposing input array to store the sums of the previous subarrays. O(1) space

    return max(nums)




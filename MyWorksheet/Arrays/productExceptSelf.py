## Problem: Given a list of integers, return a list such that, for every A[i], result[i] contains
## the product of all numbers in the list except itself.

## Solution: This is a DP problem -> we can break down the product of all numbers
## except self like this => product_except_self = product_of_left_elems * product_of_right_elems
## We can make two arrays for left and right product and multiply them to get return array.
## But for O(1) solution (excluding return array) we can simply reuse return array for left and right prod.


def product_except_self(nums):
    ret = [1] * len(nums)

    ## Iteratively compute the left product
    for i in range(1, len(nums)):
        ret[i] = ret[i-1] * nums[i-1]
    
    ## Iteratively compute the right product, starting from the end of the array
    R = 1 ## This contains right product.
    for i in range(len(nums) - 1, -1, -1):
        ret[i] = ret[i] * R
        R *= nums[i]
    return ret

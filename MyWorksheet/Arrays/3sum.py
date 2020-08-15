## Problem: Given a list of numbers, find all triplets within the list that add up to 0.

## Solution: A naive solution would be to use the two-sum logic, and check
## if there exists for a pair that sum up to x, -x in the list.
## We can optimize this approach by sorting the list and using two pointers.
## We know that for a triplet to exist, there must be negative and positive elements
## Hence, we can check if num at pointer1 + curr_elem + num at pointer2 == 0
## If it is less, we advance left pointer. If it is more we advance right pointer
## Avoid duplicate triplets by not considering values we have already considered.


def threeSum(nums):
    triplets = []

    n = len(nums)

    if n < 3:
        return []
    
    def twoSum(target, left):
        nonlocal nums, triplets
        right = n - 1
        while left < right:
            sum_vals = nums[left] + nums[right]
            #print(target, nums[left], nums[right])
            if sum_vals == target:
                triplets.append([-target,nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
            elif sum_vals < target:
                left += 1
            else:
                right -= 1
    nums.sort()
    for i in range(n):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        twoSum(-nums[i], i+1)
    
    
    return triplets

if __name__ == "__main__":
    arr = [1, 0, -1, 2]

    print(threeSum(arr))


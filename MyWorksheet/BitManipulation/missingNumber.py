## Problem: Given a list of numbers, where each number is taken from 0-N, where N is unknown,
## find the number missing in the sequence.
## It is guaranteed that there is only one missing number
## Do this using no additional space and in O(N) time.

## Solution: Bit manipulation; we use the fact that XOR is its own inverse to finding the number.
## If we set the initial number to N, we can XOR this number repeatedly with the index of curr
## element and the element itself. The resulting number must be the missing one.


def missing_number(nums):
    missing = len(nums)

    for i, num in enumerate(nums):
        missing ^= i ^ num
    
    return missing

if __name__ == "__main__":
    nums = [5,6,7,8,4,2,1,0]

    print(missing_number(nums))
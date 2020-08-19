## Problem: Given a rotated sorted array, find the min element in O(log N)

## Solution: Modified binary search
## What are the conditions?
## l = 0, r = N-1
## If arr[mid] > arr[mid+1]:
##      Return arr[mid + 1]
## Else:
##      If arr[mid] < arr[l]:
##          r = mid - 1
##      Else:
##          l = mid + 1

def minRotatedSortedArr(nums):

    l = 0
    r = len(nums) - 1 #8

    if nums[l] < nums[r]:
        return nums[l]


    while l <= r:
        mid = l + (r - l) // 2
        #print(nums[l], arr[mid], arr[r])

        if nums[mid] > nums[mid+1]:
            return nums[mid+1]
        else:
            if nums[mid] < nums[l]:
                r = mid - 1
            else:
                l = mid + 1


if __name__ == "__main__":
    arr = [7,8,9,10,2,3,4,5,6]

    print(minRotatedSortedArr(arr))

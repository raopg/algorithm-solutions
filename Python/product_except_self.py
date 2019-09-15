'''The problem: Given an array of N integers(N>1), return an array containing the products of the array except the number itself.
    Time complexity requirements: O(N)
    You CANNOT use DIVISION. Easiest solution is to reduce the list to a product and divide each number by it.
    Provide a O(1) space complexity solution if you can.
'''
#First Solution: O(N) time, O(N) space
def solution(nums : List[int]):
    '''Initialize left, right and result lists. For the left array, each element represents the product of all elements to the left, and so on for the right list.'''
    length = len(nums)
    L = [0] * length
    R = [0] * length
    result = [0] * lenght

    L[0] = 1 # Nothing to the left of L[0].
    for i in range(1, length):
        L[i] = L[i-1]* nums[i-1]

    R[length-1] = 1
    for i in reversed(range(length-1)): # We have to go in reverse because its an incremental process Right to left.
        R[i] = R[i+1] * nums[i+1]

    for i in range(length):
        result[i] = L[i] * R[i] #Multiply these together to get the result.

    return result


def solution_linear_space(nums : List[int]):
    ''' To solve the space complexity issue, we just use one result array. Since its multiplication, we just multiply existing result[i] value with new values.'''

    length = len(nums)
    result = [1] * length

    for i in range(1, length):
        result[i] = result[i-1] * nums[i-1]
    
    R = 1
    for i in reversed(range(length)):
        result[i] = result[i] * R
        R *= nums[i]

    return result




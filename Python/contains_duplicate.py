'''The Problem: Given a list of integers,(or it can be strings too), find out whether it contains a duplicate.'''

'''Solution 1: Sort the array[accepted]. Then sweep the list to see if any adjacent elements are same.
    Time complexity = O(nlogn) + O(n)
    Solution is listed below'''
import timeit

def contains_duplicate_sort( nums:List[int] ):
    nums.sort() # Python 3.x uses QuickSort. Time complexity: O(nlogn)

    for i in range(len(nums)):
        if(nums[i] == nums[i+1]):
            return True
        
    return False
def contains_duplicate_hash( nums:List[int] ):
    values = set() #Python 3.x uses a HashSet. Lookups are O(1)

    for n in nums:
        if n in values: # The in operator is O(1) in Python 3.x. The __contains__ function of the set is called in the in operator implementation.
            return True
    return False




    

    
## Given an unsorted array, sort it using a merge sort approach.

## General approach here: This is a classic D/C algorithm. We split the input array into
## two subarrays, and we recurse on each of them. Each recursive call will return a 
## a sorted subarray. We then define a merge subroutine, where we interleave
## both sorted subarrays into the resultant array.

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2

        # Make a recursive call on each subarray
        L = arr[:mid]
        R = arr[mid:]
        merge_sort(L)
        merge_sort(R)

        ## Merge both sorted subarrays
        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        
        ## Clean up any remaining elements
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
        
        return arr


if __name__ == "__main__":
    arr = [4,1,7,2,8,21,0,3,16,8]
    merge_sort(arr)
    print(arr)


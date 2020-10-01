class Solution:
    def threeSumMulti(self, A: List[int], target: int) -> int:
        count = 0
        for i in range(len(A)):
            l = i + 1
            r = len(A) - 1
            
            while l < r:
                curr_sum = A[l] + A[r] + A[i]
                
                if curr_sum == target:
                    count += 1
                    l += 1
                    r -= 1
                elif curr_sum < target:
                    l += 1
                else:
                    r -= 1
            
        
        return count

if __name__ == "__main__":
    s = Solution()

    s.threeSumMulti([])
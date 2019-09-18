class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}
        
        result = []
        
        def combine_recursive(combined, digits_left): ## Implementing a recursive function within the solution function.
            if not digits_left: ## If there are no more digits left to consider, we add the latest combination to the result, and return.
                result.append(combined) 
                return
            else:
                for char in phone[digits_left[0]]: ## First digit left to deal with
                    combine_recursive(combined + char, digits_left[1:]) ## Add the newly combined letter and make the call to the rest of the string.
            
        if not digits:
            return []
        
        combine_recursive('', digits)
        return result
## Problem: given two linked lists representing numbers, add them into a resulting LL
## Example: 1 -> 2 -> 3 and 3 -> 4 -> 5 should result in 4 -> 6 -> 8

## Solution: We simply iterate through both linked lists and add the val of each. We also maintain
## a carry value, representing any overflows in single-digit addition we need to account for in the next
## listNode.

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next


def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    result = ListNode(0)
    result_tail = result
    carry = 0
            
    while l1 or l2 or carry:            
        val1  = (l1.val if l1 else 0)
        val2  = (l2.val if l2 else 0)
        carry, out = divmod(val1+val2 + carry, 10)    
                    
        result_tail.next = ListNode(out)
        result_tail = result_tail.next                      
        
        l1 = (l1.next if l1 else None)
        l2 = (l2.next if l2 else None)
            
    return result.next

## Follow up: Given that the LLs represent the numbers in a forward manner, how would you solve this problem?
## Example: 1->2->3 represents 123, not 321, hence the carry needs to move backwards, not forwards.

def addTwoNumbersForward(l1: ListNode, l2: ListNode) -> ListNode:
    
## Problem: Given a linked list, determine if it is a palindrome.

## Solution: A very simple solution involes a two-pass approach, where we first iterate to the mid point of
## the linked list. We can then advance both pointers and check if their values are equal.

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
def palindrome(head: ListNode) -> bool:
    fast = slow = head

    stack = []

    while fast != None and fast.next != None:
        stack.append(slow.val)
        slow = slow.next
        fast = fast.next
    
    if fast != None:
        slow = slow.next
    
    while slow != None:
        if stack.pop() != slow.val:
            return False
        slow = slow.next
    
    return True



    


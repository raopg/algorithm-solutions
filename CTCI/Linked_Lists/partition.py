## Problem: Implement an algorithm to partition a linked list around a value x,
## such that all values less than x come to the left of x and all values greater 
## than or equal to x come to the right of x.

## Solution:
## A very simple approach is to create two pointers, left and right that points to two partitioned linked lists
## When we encounter a value less than x we add it to left and when we find a value greater than or equal to x
## we add it to right.

def partition(head: ListNode, x: int) -> ListNode:
    left_head = ListNode()
    right_head = ListNode
    left = left_head
    right = right_head

    temp = head

    while temp != None:
        if temp.val < x:
            left.next = temp
            temp = temp.next
            left = left.next
            left.next = None
        else:
            right.next = temp
            temp = temp.next
            right = right.next
            right.next = None
        
    left.next = right_head.next
    return left_head.next
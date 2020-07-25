## Problem: Implement an algorithm to find the kth ot last element of a singly
## linked list.

## Solution: Obviously a trivial solution would be compute the length of the linked list
## and iterate through N- k nodes.

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

def linkedListLength(head: ListNode) -> int:
    count = 0

    while head != None:
        count += 1
        head = head.next

def KthToLast(head: ListNode, k: int) -> ListNode:
    temp = head
    length = linkedListLength(head)
    target = length - k + 1

    while target != 0:
        temp = temp.next
        target -= 1
    return temp

## More optimatal solution -> Place two pointers, p1 and p2 at k distance apart, starting from the head.
## Then iterate till p2 == None. Return p1

def KthToLastOptimal(head: ListNode, k: int) -> ListNode:
    p1 = p2 = head

    if head == None:
        return None

    for i in range(k):
        p2 = p2.next
        if p2 == None:
            return None
    
    while p2 != None:
        p1 = p1.next
        p2 = p2.next

    return p1
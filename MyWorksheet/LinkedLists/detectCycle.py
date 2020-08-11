## Problem: Given a linked list, find out whether there is a cycle present.

## Solution: One possible solution would be to maintain a hashset of all values that we have seen before
## and see if any of those values gets repeated.

from LL import *
import unittest

def findCycle(head: ListNode) -> bool:
    seen = set()
    temp = head
    
    while temp != None:
        if temp.val in seen:
            return True
        seen.add(temp.val)

    return False

## Alternative => What if there are duplicate values? this is harder in python, because we do not actively
## deal with object addresses. One solution is to overload the == operator. This also makes the object unhashable,
## so we need to implement a hash function as well.

class HashableListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
    def __eq__(self, other):
        if not isinstance(other, ListNode):
            return False
        return other.val == self.val and other.next == self.next
    
    def __hash__(self):
        return hash((self.val, self.next))

## this definition of listnode will help us tackle duplicate nodes problem.

## In this case, we store the ListNode itself in our hashtable
def detectCycle(node: 'HashableListNode') -> bool:
    seen = set()

    if not node:
        return True
    
    while node:
        if node in seen:
            return True
        seen.add(node)
    
    return False
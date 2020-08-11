## Problem: Given two sorted linked lists, merge them into one sorted linked list.
## Do this in constant space

## Solution: Much like merge sort, simply have two pointers for the linked lists. Move each
## pointer along when it is the lower value.
## Use a header linked list for result, since we don't know beforehand the first node

## Time Complexity: O(M+N) time, where M, N are the sizes of the lists, O(1) space.

from LL import *
import unittest

def mergeLinkedList(list1: 'LinkedList', list2: 'LinkedList'):
    ## Make the header
    new_ll = LinkedList()
    new_ll.head = ListNode()
    temp = new_ll.head()

    ## While there are nodes in both lists
    while list1 and list2:
        if list1.val <= list2.val:
            temp.next = list1
            list1 = list1.next
        else:
            temp.next = list2
            list2 = list2.next
        temp = temp.next
    ## After loop, if there are any remaining nodes in list1 (implies list2 == None)
    if list1:
        temp.next = list1
    ## Similarly check for list2
    if list2:
        temp.next = list2

    ## Remove the header node
    new_ll.head = new_ll.head.next
    return new_ll

class TestMergeLinkedLists(unittest.TestCase):
    pass


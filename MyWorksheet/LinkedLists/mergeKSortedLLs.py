## Problem: Given a list of linked lists, merge all of them into one sorted linked list

## Solution: Consider a similar approach to merging two lists.
## Obviously, we can call merge_two_LLs in a loop. That would result in a O(kN) algorithm
## Another approach -> Iterate thru all nodes in all LLs, store it in an array, sort it, and build a list from that
## Time-space of that would be O(NlogN) time, O(N) space (brute-force)

## The first approach is actually on the right track. We can optimize this further -> pair up the K lists
## and merge them. This results in K/2 lists that need to be merged further. Repeatedly do this till we have
## one list. Time complexity -> O(N * logK) -> because we pair N nodes every time, logK times.

from LN import *

## First approach -> O(kN) time.

def mergeKLists(lists) -> 'ListNode':
    if not lists:
        return None
    
    merged = lists[0]

    for i in range(1, len(lists)):
        merged = mergeTwoLists(merged, lists[i])
    
    return merged

def mergeTwoLists(list1, list2):
    new_list = ListNode()
    temp = new_list

    while list1 and list2:
        if list1.val <= list2.val:
            temp.next = list1.val
        else:
            temp.next = list2.val
        temp = temp.next
    
    if list1:
        temp.next = list1
    if list2:
        temp.next = list2
    
    return new_list.next


def mergeKListsOptimized(lists) -> 'ListNode':
    if lists is None:
        return None
    
    length = len(lists)
    interval = 1

    while interval < length:
        for i in range(0, length - interval, interval * 2):
            lists[i] = mergeTwoLists(lists[i], lists[i + interval])
        interval *= 2
    return lists[0]


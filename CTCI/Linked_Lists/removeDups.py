## Problem: Given a linked list, remove all the duplicates.

## Solution: We can simply maintain a HashSet of the visited nodes and remove a node if its data is ever repeated.

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

def removeDups(head: ListNode) -> ListNode:
    ''' Given a singly LL, remove all duplicate nodes'''

    temp = ListNode()
    temp.next = head
    seen = set()

    ## Edge cases
    if head == None or head.next == None:
        return head

    while temp.next != None:
        if temp.next.val in seen:
            toDelete = temp.next
            temp.next = temp.next.next
            del toDelete
        else:
            seen.add(temp.next.val)
    
    return head

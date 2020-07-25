## Problem: Given a linked list, remove all the duplicates.

## Solution: We can simply maintain a HashSet of the visited nodes and remove a node if its data is ever repeated.
## Time and Space Complexity: O(N) and O(N)

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

## Follow-up: Remove duplicates no space -> we have to sacrifice time.

def removeDuplicateNoSpace(head: ListNode) -> ListNode:
    temp = head
    
    while temp != None:
        lookahead = temp
        while lookahead.next != None:
            if lookahead.next.val == temp.val:
                lookahead.next = lookahead.next.next
            else:
                lookahead = lookahead.next
        temp = temp.next
    
    return head

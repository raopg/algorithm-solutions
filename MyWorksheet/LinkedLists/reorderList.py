## Problem: Given a linked list, write an algorithm to reorder a list such that
## the nodes at the beginning and nodes at the end are interleaved.
## Ex: first->second->...->last becomes first->last->second->second-last->....->middle


## Solution: First, use a fast and slow pointer to get to the middle of the LL.
## Then use a stack to add all node from mid to end.
## Then, "merge" the two sublists by alternatively choosing from the start or the stack.
## Be sure to take care of edge cases.
from LL import *
def reorder(head):
    fast = slow = head

    while fast and fast.next != None:
        fast = fast.next.next
        slow = slow.next
    
    if fast: ## LL length is odd
        slow = slow.next
    
    stack = []
    while slow:
        stack.append(slow)
        slow = slow.next

    new_head = ListNode()
    temp = new_head
    old_list = head
    i = 0
    while stack and old_list:
        if i % 2 == 0:
            temp.next = old_list
            old_list = old_list.next
        else:
            node = stack.pop(-1)
            node.next = None
            temp.next = node
            
        temp = temp.next
        i += 1
    if old_list: ## There is an extra node, its an odd sized list
        temp.next = old_list
        old_list.next = None
    return new_head.next

if __name__ == "__main__":
    l = LinkedList()
    for val in [1,2,3,4,5,6,7,8]:
        l.addNode(val)
    
    new_ll = LinkedList()

    new_ll.head = reorder(l.head)
    print(new_ll)
    

        


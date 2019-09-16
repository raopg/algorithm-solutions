''' The Problem: Given a linked-list, and a number n, delete the nth node from the end of the list and return the head'''

class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next
    
def remove_nth_node_fromend(head, n):
    prev = new ListNode(0, head) # Dummy node at the front.
    temp = prev
    to_delete = prev

    for i in range(n):
        temp = temp.next # We let the temp pointer get a headstart of exactly n nodes.
    
    while temp != None:
        temp = temp.next
        to_delete = to_delete.next

    to_delete.next = to_delete.next.next # Current to_delete.next is the node we want to delete.

    return prev.next # The head of the Linked list
    
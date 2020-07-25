## Problem: Implement an algorithm to delete a node in the middle of a linked list
## This can be any node - not the first or the last, BUT, you are only given access to that node.


## Solution: We can simply copy the value of the next node into the node to be deleted, and delete the next node.
class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

def deleteMiddleNode(node: ListNode) -> None:
    if node == None or node.next == None:
        return
    node.val = node.next.val
    to_delete = node.next
    node.next = node.next.next
    del to_delete

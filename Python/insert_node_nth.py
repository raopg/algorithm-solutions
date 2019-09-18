### The Problem: Given a linked list, data and an index, insert a node into the linked list at that index.

class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next

def solution(head, data, position):
    i = 0

    if head == None:
        return ListNode(data)
    temp = ListNode(0)
    temp.next = head

    while temp.next != None and i != position:
        temp = temp.next
        i += 1
    temp.next = current_next
    new_node = ListNode(data)
    temp.next = new_node
    new_node.next = current_next
    
    return head
    

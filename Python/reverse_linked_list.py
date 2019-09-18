## Given the head of the Linked List, reverse it. [In place is preferred]


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    

def solution(head):
    temp = head
    prev = None

    while temp != None:
        next_node = temp.next
        temp.next = prev
        prev = temp
        temp = next_node
    
    return prev


## Given two Linked lists, check if they are equal => each node has the same data and is in the same position.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def solution(llist1, llist2):
    temp1, temp2 = llist1, llist2

    while temp1 != None and temp2 != None:
        if temp1.val != temp2.val:
            return False

    if temp1 or temp2:
        return False
    return True

## Time Complexity: O(min(m,n)), where m and n are the lengths of the linked lists.
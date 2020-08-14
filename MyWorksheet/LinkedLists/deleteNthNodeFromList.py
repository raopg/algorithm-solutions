## Problem: Given a linked list, delete the N-th last node.

## Solution:
## We can simply compute the length of the LL with one-pass. Then, FF a pointer to L - N + 1 'th node.
## a -> b -> c -> d -> e -> f, N = 2 => L(6) - N(2) + 1 => 5th node. With zero based indexing it is 4th node.
## We want to access this node's previous => L - N - 1 is the prev node, L - N is the node to be deleted.

from LL import *
def deleteNthNodeFromLast(ll, N):

    if ll is None:
        return None
    
    ## Compute the length.
    temp = ll
    length = 0
    while temp != None:
        length += 1
        temp = temp.next
    
    ## Iterate
    prev = ll
    for i in range(length - N):
        prev = prev.next

    ##Delete next node
    prev.next = prev.next.next

    return

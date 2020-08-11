## Problem: Given a linked list node and new value, add a new node next to it.

from LL import *
import unittest

def addNodeInMiddle(node: 'ListNode', val) -> None:
    ''' Given access to some random node in the linked list, add a node next to it. '''
    new_node = ListNode(val)
    temp = node.next
    node.next = new_node
    new_node.next = temp

class TestAddNodeInMiddle(unittest.TestCase):
    pass

if __name__ == "__main__":
    pass
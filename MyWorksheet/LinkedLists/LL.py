## This is the first file for this module. The goal is to create basic LL structures and functions that the
## rest of the modules can import

import unittest

class ListNode:
    def __init__(self, val = 0, n = None):
        self.val = val
        self.next = n

class LinkedList:
    '''Basic LinkedList class with methods to add, delete and print the Linked List'''
    def __init__(self, head = None):
        self.head = head
    
    def __str__(self):
        temp = self.head
        nodes = []
        if temp == None:
            return 'None'
        while temp:
            nodes.append(str(temp.val))
            temp = temp.next
        
        nodes.append('None')

        return '->'.join(nodes)
    
    def __repr__(self):
        return '<LinkedList> ' + self.__str__()
    
    def addNode(self, val):
        new_node = ListNode(val)
        
        if not self.head:
            self.head = new_node
            return

        temp = self.head
        while temp.next != None:
            temp = temp.next
        
        temp.next = new_node
    
    def deleteNode(self, val):
        '''Given a value, delete all instances of that value in the LL'''
        if not head:
            raise Exception("Cannot delete from empty LL")
        temp = head
        prev = None
        while temp:
            if temp.val == val:
                to_delete = temp
                temp = temp.next
                del to_delete

                if prev:
                    prev.next = temp
                #break ## Uncomment this if you want to delete the first instance of the val
        return

class TestLinkedList(unittest.TestCase):
    def testAdd(self):
        ll = LinkedList()
        nodes = [1,5,12,2]

        for n in nodes:
            ll.addNode(n)
        
        self.assertEqual(str(ll), '->'.join(nodes) + 'None')
    def testStr(self):
        ll = LinkedList()
        self.assertEqual(str(ll), 'None')

            
    
    

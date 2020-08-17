## Problem: Implement the hashSet class.

## Solution: We can use an array of buckets to keep the values
## We can handle collisions by using a linked list in each bucket.
## The number of buckets is ideally a large prime. Ex: 769

class ListNode:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next
class HashSet:
    def __init__(self):
        self.BUCKET_SIZE = 769
        self.buckets = [ListNode() for _ in range(self.BUCKET_SIZE)]
    
    def hash(self, val):
        return val % self.BUCKET_SIZE
    
    def add(self, val):
        bucket = self.hash(val)

        temp = self.buckets[bucket]
        while temp.next != None:
            temp = temp.next
        temp.next = ListNode(val)
    
    def remove(self, val):
        bucket = self.hash(val)

        temp = self.buckets[bucket]
        while temp.next != None:
            if temp.next.val == val:
                to_delete = temp.next
                temp.next = temp.next.next
        
    
    def contains(self, val):
        bucket = self.hash(val)

        temp = self.buckets[bucket]

        while temp.next != None:
            if temp.next.val == val:
                return True
        
        return False
        

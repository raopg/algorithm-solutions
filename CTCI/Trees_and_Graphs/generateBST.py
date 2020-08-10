## Problem: Given a sorted list, create a binary search tree with minimal height

## Solution: Use a binary search approach -> keep dividing the array in the middle recursively.

class TreeNode:
    def __init__(self, val = 0):
        self.val = val
        self.left = None
        self.right = None

def inOrderTraversal(root):
    if root is None:
        return
    inOrderTraversal(root.left)
    print(root.val, end = " ")
    inOrderTraversal(root.right)

def generateBST(arr):
    if not arr: return None

    if len(arr) == 1:
        return TreeNode(arr[0])

    mid = len(arr) // 2

    root = TreeNode(arr[mid])
    root.left = generateBST(arr[:mid])
    root.right = generateBST(arr[mid+1:])

    return root

if __name__ == "__main__":
    arr = [1,2,3,4,5,6,7,8,9,10]
    generatedTree = generateBST(arr)
    inOrderTraversal(generatedTree)


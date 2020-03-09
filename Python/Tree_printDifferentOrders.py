## Simple code to print a Tree in 3 different orders:
## 1. Preorder - print the current node and its leaves later.
## 2. Inorder - print the left leaf, current node and right leaf in that order
## 3. Postorder - print both leaves first, then print the current node.

class Tree:
    def __init__(self, info = 0,left = None, right = None):
        self.info = info
        self.left = left
        self.right = right


def preOrder(root):
    if root == None:
        return
    else:
        print(root.info, '', end='') ## To print in the format of -> 1 2 3 4 5
        preOrder(root.left)
        preOrder(root.right)

def inOrder(root):
    if root == None:
        return
    else:
        inOrder(root.left)
        print(root.info, '', end='') ## To print in the format of -> 1 2 3 4 5
        inOrder(root.right)

def postOrder(root):
    if root == None:
        return
    else:
        postOrder(root.left)
        postOrder(root.right)
        print(root.info, '', end='') ## To print in the format of -> 1 2 3 4 5



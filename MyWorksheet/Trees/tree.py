## This is the first file in the Trees module. This will contain TreeNode and Tree classes.
## The tree class will implement functions such as depth/height, size and order-based traversal

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val
        self.left = left
        self.right = right

class Tree:
    def __init__(self, root = None):
        self.root = root
    
    def size(self):
        return self._size_recursive(self.root)
    
    def height(self):
        return self._height_recursive(self.root)
    
    def depthOfNode(self, val):
        return self._depth_recursive(self.root, val, 0)
    
    def isBalanced(self):
        return self._is_balanced_recursive(self.root)
    
    def isBST(self):
        return self._is_bst_recursive(self.root, float("inf"), float("-inf"))

    def _size_recursive(self, node: 'TreeNode'):
        if node == None:
            return 0
        else:
            return 1 + self._size_recursive(node.left) + self._size_recursive(node.right)
    
    def _height_recursive(self, node: 'TreeNode'):
        if node is None:
            return -1
        else:
            return 1 + max(self._height_recursive(node.left), self._height_recursive(node.right))
    
    def _depth_recursive(self, node, val, curr_depth):
        if node is  None:
            return -1
        if node.val == val:
            return curr_depth
        return max(self._depth_recursive(node.left, val, curr_depth + 1), \
            self._depth_recursive(node.right, val, curr_depth + 1))

    def _is_balanced_recursive(self, node):
        if node is None:
            return True
        return abs(self._height_recursive(node.left) - self._height_recursive(node.right)) < 2 \
            and self._is_balanced_recursive(node.left) and self._is_balanced_recursive(node.right)
    
    def _is_bst_recursive(self, node, min_val, max_val):
        if node is None:
            return True
        if node.val <= min_val or node.val > max_val:
            return False
        
        return self._is_bst_recursive(node.left, min_val, node.val) and \
            self._is_bst_recursive(node.right, node.val, max_val)
    
    
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
    
    def traversal(self, type = 'in-order'):

        if type == 'post-order':
            return self._postorder_traversal(self.root)
        elif type == 'pre-order':
            return self._preorder_traversal(self.root)
        elif type =='level-order':
            return self._level_order_traversal(self.root)
        elif type =='level-order-zigzag':
            self.levels = []
            self._level_order_zigzag_traversal(self.root)
            return self.levels
        else:
            return self._inorder_traversal(self.root)


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
    
    ## Traversal helpers

    def _inorder_traversal(self, root):
        if not root:
            return
        if root.left:
            self._inorder_traversal(root.left)
        print(root.val)
        if root.right:
            self._inorder_traversal(root.)
    def _preorder_traversal(self, root):
        if not root:
            return
        print(root.val)
        if root.left:
            self._preorder_traversal(root.left)
        if root.right:
            self._preorder_traversal(root.right)
    def _postorder_traversal(self, root):
        if not root:
            return
       
        if root.left:
            self._postorder_traversal(root.left)
        if root.right:
            self._preorder_traversal(root.right)
        print(root.val)
    def _level_order_traversal(self, root, level):

        if not root:
            return
        
        if len(self.levels == level):
            levels.append([])
        
        levels[level].append(root.val)
        
        if root.left:
            self._level_order_traversal(root.left, level + 1)
        if root.right:
            self._level_order_traversal(root.right, level + 1)

    def _level_order_zigzag_traversal(self, root):
        pass
    
# Question: Given a binary tree, return the number of  nodes that are 'good' nodes.

# A 'good' node is one where its value is greater than that of all nodes
# from itself to the root.

## Solution approach: A node's value will be the highest of its path to
## the root if it is greater than the maximum node in that path.
## So, we can recursively maintain the max-val of the path thus far,
## and just compare with the node's val to see if it is good.

## A child node of a non-good node can still be a good node, if its val
## greater than that of all nodes.

def goodNodes(root):

    def goodNode(root, max_val):
        if root == None:
            return 0
        count = 0
        if root.val > max_val:
            max_val = root.val
            count += 1
        return count + goodNode(root.left, max_val) + goodNode(root.right, max_val)

    return goodNode(root, float('-inf'))
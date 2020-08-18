## Problem: Given a connected, undirected graph, return a deepcopy clone of the graph.
## The definition of a graph is given.

from graph import GraphNode

class Solution:
    def __init__(self):
        self.visited = dict()

    def clone(self, node: 'GraphNode'):
        if not node:
            return None
        
        if node in self.visited:
            return self.visited[node]

        clone_node = GraphNode(node.val, [])
        self.visited[node] = clone_node

        if node.neighbors:
            clone_node.neighbors = [self.clone(n) for n in node.neighbors]
        
        
        return clone_node
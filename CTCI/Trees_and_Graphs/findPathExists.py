## Problem: Given a graph and two nodes contained in the Graph, determine if there exists a path between them
from collections import deque
def GraphNode:
    def __init__(self, val, neighbors = set()):
        self.val = val
        self.neighbors = neighbors

def Graph:
    def __init__(self):
        self.graph = dict()
    
    def findPathExists(self, node1: GraphNode, node2: GraphNode) -> bool:
        q = deque()
        q.append(node1)
        visited = set()
        while q:
            node = q.pop()
            if node is node2:
                return True
            if node not in visited:
                q.extend(list(node.neighbors))
                visited.add(node)
        
        return False

if __name__ == "__main__":
    g = Graph()
    g.graph[]
            



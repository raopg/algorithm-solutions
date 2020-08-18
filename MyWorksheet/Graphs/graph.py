## Basic Implmentation of Graph DS for:
## 1. Adj list
## 2. Adj matrix
## For each of the above, undirected weighted, directed weighted, and non-weighted graph implementations.

class GraphNode:
    def __init__(self, val= 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors

class Graph:
    def __init__(self):
        self.graph = [GraphNode()]

## OR, we can simply represent Graphs as a dictionary mapping node to neighbors.
from collections import defaultdict
class GraphSimple:
    def __init__(self):
        self.graph = defaultdict(list) ## Or defaultdict(set)
    
    def add_edge(self, u, v):
        self.graph[u].append(v)
    
    def dfs(self, start_node):
        visited = set()

        def helper(node):
            nonlocal visited
            if not node:
                return
            
            ## Do what you need to do with the DFS. This is a simple version, I will just print
            print(node)

            visited.add(node)

            for child in self.graph[node]:
                if child not in visited:
                    helper(child)

        helper(start_node)

    def bfs(self, start_node):
        visited = set()

        q = [] ## collections.deque prob better if we want appendleft etc.

        if not start_node:
            q.append(start_node)
        
        while q:
            node = q.pop(0)
            print(node)
            visited.add(node)

            for child in self.graph[node]:
                if child not in visited:
                    q.append(child)
        



            


    
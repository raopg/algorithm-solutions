## Problem: Given an undirected graph, find the number of connected components.
## Solution: We can start with an equivalence relation for each connected components.
## The equivalence relation is that for u,v in G, there exists a path u-v in G.
## For all groups of nodes that combine for the equivalence relation, they form a connected component.
from collections import defaultdict
def count_connected(connections):
    nodes = set()
    adj_list = defaultdict(set)
    for u,v in connections:
        nodes.add(u)
        nodes.add(v)
        adj_list[u].add(v)
        adj_list[v].add(u)
    
    visited = set()
    count = 0
    for node in nodes:
        if node in visited:
            continue
        count += 1
        q = [node]
        while q:
            n = q.pop(0)
            visited.add(n)
            for neighbor in adj_list[n]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    q.append(neighbor)
    
    return count

if __name__ == "__main__":
    ##  
    ##  1 - 2, 3, 4
    ##  2 - 1, 5
    ##  3 - 1
    ##  4 - 1, 5
    ##  5 - 2, 4
    ##  10 - 12, 13
    ##  12 - 10
    ##  13 - 10

    edges = [(1,2),(1,3),(1,4),(2,5),(4,5),(10,12),(10,13)]

    print(count_connected(edges))
## What: Ordering of the vertices of the directed acyclic graph, such that the vertices
## only go forward. Meaning in a list of vertices from L to R, the ordering
## of the vertices must match the ordering of the edges.
## If there is a vertex u where List[i] = u, which has
## a directed edge to v, where List[j] = v, then i MUST be less than j.

## Applications: Course prerequesites. We need all of the pre-req courses to occur
## before the next courses, and we can use topo sorting.
## You CANNOT topologically sort a cyclic graph. It's pretty obvious - you cannot come up with an
## ordering where the condition is satisfied.
## If a graph is acyclic, you are guaranteed a topological ordering.

from collections import defaultdict, deque

def recursive_topo_sort(v, visited, adj_list, stack):
    visited.add(v)

    for i in adj_list[v]:
        if i not in visited:
            recursive_topo_sort(i, visited, adj_list, stack)
    
    stack.appendleft(v)

def topological_sort(n, edges):
    adj_list = defaultdict(set)
    for u, v in edges:
        adj_list[u].add(v)
    
    visited = set()
    stack = deque([])

    for i in range(n):
        if i not in visited:
            recursive_topo_sort(i, visited, adj_list, stack)
    
    return list(stack)
    

if __name__ == "__main__":
    n = 6
    edges = [(5,0), (5,2), (4,0), (4,1), (2,3), (3,1)]

    print(topological_sort(n, edges))


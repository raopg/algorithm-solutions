## Implement Dijkstra's algorithm to find the shortest path between two nodes.
## Given: Obviously a weight graph. Can be directed or undirected. Our algorithm will be slightly
## different in the two cases.


## General idea: We have a greedy approach to this problem
## Graph representation - adj list where value is a list of tuples, corrsponding
## to the connecting node, AND the cost.

from collections import defaultdict
def build_adj_list(weighted_edges):
    adj_list = defaultdict(list)
    for u, v, cost in weighted_edges:
        adj_list[u].append((v,cost))
        adj_list[v].append((u, cost)) ## This is only for undirected graph.
    return adj_list

def dijkstra(weighted_edges, start_node):
    adj_list = build_adj_list(weighted_edges)

    visited = set()
    costs = defaultdict(lambda: float('inf'))
    costs[start_node] = 0
    q = [start_node]

    while q:
        node = q.pop(0)
        if node in visited:
            continue
        visited.add(node)

        for nei, cost in adj_list[node]:
            if costs[node] + cost < costs[nei]:
                costs[nei] = costs[node] + cost
                q.append(nei)
    
    return costs

if __name__ == "__main__":
    weighted_edges = [(1,2,2), (1,3,4), (2,4,7), (3,5,3), (2,3,1), (4,5,2), (4,6,1), (5,6,5)]
    start_node = 1

    print(dijkstra(weighted_edges, start_node))



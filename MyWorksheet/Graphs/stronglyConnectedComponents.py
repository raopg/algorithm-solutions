## Idea: We know what connectivity means in an undirected graph.
## But, in a directed graph, connectivity is not the same
## Although there exists a connection from node A to node B if there is a 
## a directed edge between A and B, you can't say that you can go from any
## point to another in a connected set of nodes (cause directed edges)

## A graph/component is strongly connected if you can go from any node to any other
## node in a DIRECTED graph/component. There is no point discussing strong connectivity
## in a undirected graph.
## Problem: List the strongly connected components (SCC) of a graph.

## Solution: We use DFS. Why?
## because we can find a cycle (which essentially discovers a SCC)
## But we cannot discover the whole graph or a union of SCCs.
## We need to find nodes in the graph where, if we do a DFS, we find only ONE SCC.

## So, the solution has 2 parts (Kosaraju's Two-Pass Algorithm):
## 1. Using a precompute subroutine, find all the starting nodes which, when we perform
## DFS on, gives us exactly ONE SCC.
## 2. Iterate thru these list of nodes and perform DFS on each one. Combine all SCCs into a list
## Time complexity = O(m + n)
## Space = O(m + n)

## Kosaraju Algorithm Details.
## 1. Compute the reverse of the given graph G -> invert all directed edges.
## 2. Run a DFS on rev(G) (outer loop thru all nodes cause we need to find disconnected graph components also)
## 3. Run a DFS on G.

## The idea is this: For the DFS to execute perfectly and get the strongly connected components, the
## DFS must execute in a very particular order. The DFS on the rev(G) provides this magical ordering for us.
## What is this magical ordering?
## We use the notion of a "finishing time" on the vertices.
## We perform the DFS on nodes ordered by decreasing finishing times.
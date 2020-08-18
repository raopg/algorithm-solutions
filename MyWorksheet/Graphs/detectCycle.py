## Problem: Given a graph, detect if there is a cycle present.
## Solve this problem for both adj_list and adj_matrix representations of a graph

from graph import *

def detect(g: 'GraphSimple', start_node: 'GraphNode', stack):
    stack.add(start_node)
    for child in g.graph[start_node].children:
        if child in stack:
            return True
        if detect(g, child, stack):
            return True
    stack.remove(start_node)

    return False

def detect_cycle(g: 'GraphSimple', start_node: 'GraphNode'):
    return detect(g, start_node, set())



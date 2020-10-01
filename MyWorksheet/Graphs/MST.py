## Given a graph, find the min.spanning tree.

## Solution: Two approaches - using Kruskal UF or Prim Algo

class DSU:
    def __init__(self, N):
        self.parent = [i for i in range(N)]
        self.size = [1] * N
    def find(self, x):
        if self.parent[x] == x:
            return x
        return self.find(self.parent[x])
    
    def union(self, x,y):
        par_x, par_y = self.find(x), self.find(y)
        if par_x == par_y:
            return False
        if self.size[par_x] < self.size[par_y]:
            par_x, par_y = par_y, par_x
        
        self.parent[par_y] = par_x
        self.size[par_x] += self.size[par_y]
        self.size[par_y] = 0

        return True

def minimum_spanning_tree(N, edges):
	d = DSU(N) # Create the DSU for the number of vertices
	
	## Sort the edges by increasing weight
	## Greedily pick lowest weight edges till graph is completely connected.
	
	edges.sort(key = lambda x: x[2])
	
	tree_edges = []
	for start, end, weight in edges:
		if d.union(start, end):
			tree_edges.append([start,end,weight])
	

	return tree_edges



if __name__ == "__main__":
    edges = [
        [0,1, 10],
        [1,2, 5],
        [0,2, 50]
    ]

    print(minimum_spanning_tree(3, edges))

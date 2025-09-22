"""
Solução para o problema "Design Graph With Shortest Path Calculator" (LeetCode 2.642)
"""


class Graph(object):
    def __init__(self, n, edges):
        from collections import defaultdict
        
        self.n = n
        self.adj = defaultdict(list)

        for u, v, w in edges:
            self.adj[u].append((v, w))

    def addEdge(self, edge):
        u, v, w = edge
        self.adj[u].append((v, w))

    def shortestPath(self, node1, node2):
        """
        Utiliza Dijkstra para calcular o caminho mais curto em um grafo direcionado com pesos.
        """
        from heapq import heappop, heappush

        INF = 10**18
        dist = [INF] * self.n
        dist[node1] = 0
        heap = [(0, node1)]

        while heap:
            d, u = heappop(heap)

            if d > dist[u]:
                continue

            if u == node2:
                return d
            
            for v, w in self.adj.get(u, []):
                nd = d + w
                
                if nd < dist[v]:
                    dist[v] = nd
                    heappush(heap, (nd, v))

        return -1 if dist[node2] == INF else dist[node2]
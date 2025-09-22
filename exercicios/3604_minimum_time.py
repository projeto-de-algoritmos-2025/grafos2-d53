"""
Solução para o problema "Minimum Time to Reach Destination in Directed Graph" (LeetCode 3.604)
"""


class Solution(object):
    def minTime(self, n, edges):
        """
        Utiliza uma variação de Dijkstra onde o custo é o tempo de chegada.
        """
        from heapq import heappop, heappush
        from collections import defaultdict

        g = defaultdict(list)

        for u, v, s, e in edges:
            g[u].append((v, s, e))

        heap = [(0, 0)]
        best = {}

        while heap:
            t, u = heappop(heap)

            if u in best and best[u] <= t:
                continue
            best[u] = t

            if u == n - 1:
                return t

            for v, s, e in g.get(u, []):
                if t > e:
                    continue

                depart = t if t >= s else s
                arrive = depart + 1

                if v not in best or arrive < best[v]:
                    heappush(heap, (arrive, v))

        return -1

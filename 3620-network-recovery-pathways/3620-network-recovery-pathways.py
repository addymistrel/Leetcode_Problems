from typing import List
import heapq

class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        n = len(online)

        graph = [[] for _ in range(n)]
        maxEdge = 0

        for u, v, w in edges:
            graph[u].append((v, w))
            maxEdge = max(maxEdge, w)

        def can(minEdge):
            INF = float("inf")
            dist = [INF] * n
            dist[0] = 0

            pq = [(0, 0)]  # (cost, node)

            while pq:
                cost, node = heapq.heappop(pq)

                if cost > dist[node]:
                    continue

                for nei, w in graph[node]:
                    if not online[nei]:
                        continue
                    if w < minEdge:
                        continue

                    newCost = cost + w
                    if newCost < dist[nei]:
                        dist[nei] = newCost
                        heapq.heappush(pq, (newCost, nei))

            return dist[n - 1] <= k

        if not online[0] or not online[n - 1]:
            return -1

        lo, hi = 0, maxEdge
        ans = -1

        while lo <= hi:
            mid = (lo + hi) // 2

            if can(mid):
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1

        return ans
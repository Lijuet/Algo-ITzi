import heapq
from math import inf

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = [[] for _ in range(n + 1)]
        dist = [inf] * (n + 1)
        dist[k] = 0
        hq = [(0, k)]
        
        for s, e, w in times: graph[s].append((e, w))
            
        
        while hq:
            d, cur = heapq.heappop(hq)
            if dist[cur] < d: continue
                
            for adj, cost in graph[cur]:
                nd = d + cost
                if nd < dist[adj]:
                    dist[adj] = nd
                    heapq.heappush(hq, (nd, adj))
            
        return -1 if inf in dist[1:] else max(dist[1:])
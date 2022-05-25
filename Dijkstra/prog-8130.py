'''
LINK : [2021 카카오 채용연계형 인턴십 > 미로 탈출](https://programmers.co.kr/learn/courses/30/lessons/81304)
OPINION :  
시간 초과나서 다시 생각해봐야한다
'''

import heapq
from copy import deepcopy

def solution(n, start, end, roads, traps):
    def switch(trap, graph):
        ng = [[] for _ in range(n + 1)]
        for s in range(n + 1):
            for e, w in graph[s]:
                if s == trap or e == trap: ng[e].append((s, w))
                else: ng[s].append((e, w)) 
        return ng
            
    answer = 0
    graph = [[] for _ in range(n + 1)]
    for s, e, w in roads: graph[s].append((e, w))
    hq = [(0, start, graph)]
    
    while hq:
        cost, cur, graph = heapq.heappop(hq)
        
        if cur == end: return cost
        if cur in traps: graph = switch(cur, graph)
        
        for adj, weight in graph[cur]:
            heapq.heappush(hq, [cost + weight, adj, deepcopy(graph)])

n, start, end, roads, traps = 3, 1, 3, [[1, 2, 2], [3, 2, 3]], [2]
print(solution(n, start, end, roads, traps))
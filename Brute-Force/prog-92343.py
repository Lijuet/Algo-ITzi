'''
LINK : [양과 늑대](https://programmers.co.kr/learn/courses/30/lessons/92343)
OPINION :
숫자가 적어서 완전탐색으로 하였다.
1. 현재 양 / 늑대 양 계산
2. 양과 늑대 수 체크
3. 갈 수 있는 모든 경로를 모두 큐에 삽입
'''

from collections import deque
from copy import deepcopy

def solution(info, edges):
    maxSh = 0
    n = len(info)
    graph = {i:[] for i in range(n)}
    
    for e in edges: graph[e[0]].append(e[1])
    
    que = deque([(0, (0, 0), [])])
    
    while que:
        cur, (sh, wo), adjs = que.popleft()
        
        if info[cur]: wo += 1
        else: sh += 1
        if sh <= wo: continue
        
        if sh > maxSh: maxSh = sh
        
        adjs.extend(graph[cur])
        
        for adj in adjs:
            next = deepcopy(adjs)
            next.remove(adj)
            que.append((adj, (sh, wo), next))
        
    return maxSh

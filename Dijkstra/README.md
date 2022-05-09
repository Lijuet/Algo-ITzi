# 다익스트라(Dijkstra)는 무엇일까?

음의 간선(Negative Edge)이 없는 그래프에서 한 노드에서 나머지 노드들까지의 최소 경로를 구하는 알고리즘입니다. 
1. 출발 노드를 정하고 최단 거리 테이블을 모두 무한으로 초기화 한다.
2. 현 노드에서 갈 수 있는 모든 노드들에 대해 다음을 반복한다.
    1. 현 노드까지의 거리 + 다음 노드까지의 간선 가중치(weight)로 새로운 거리를 계산한다.
    2. 현재 최단 거리 테이블보다 새로운 거리가 짧으면 갱신한다.
3. 방문하지 않은 노드들 중 가장 짧은 거리를 가진 노드를 방문 처리한 후 현재 노드가 된다.

# 구현 방법
3번에서 가장 짧은 거리를 가진 노드를 찾는 방법에 다양한 방법이 있다. 
1. 최단 거리 테이블을 모두 스캔하여 최소 거리를 가진 노드를 찾는다.
2. Min Heap을 이용하여 최소 거리를 가진 노드를 찾는다.

## 방법 1 : 테이블 스캔 방식
```
import math

graph = [
  [(1, 5), (2, 3)],
  [(3, 3), (2, 2)],
  [(4, 4), (5, 2), (3, 7)],
  [(4, 1)],
  [],
  [(4, 5)]
]
v = len(graph)
dist = [math.inf] * v

def Dijkstra(start):
  def getMinDistNode(): # find the not-visited node with the shortest distance
    minNode = -1
    minDist = math.inf

    for node in range(v):
      if not visited[node] and dist[node] < minDist: 
        minNode, minDist = node, dist[node]

    return minNode    
  
  dist[start] = 0
  visited = [False] * v
  
  for _ in range(v - 1):
    cur = getMinDistNode()
    visited[cur] = True
    print(cur, dist, visited)

    for adj, weight in graph[cur]:
      nd = dist[cur] + weight
      if nd < dist[adj]:
        dist[adj] = nd

Dijkstra(0)
for i in range(v): print("dist[",i,"] = ", dist[i]) # print distance
```
<b> Complexity </b>
* Time : O(V * V + E * 1) = O(V^2)
* Space : O(V)

## 방법 2 : 최소 힙 이용
```
import math
import heapq

graph = [
  [(1, 5), (2, 3)],
  [(3, 3), (2, 2)],
  [(4, 4), (5, 2), (3, 7)],
  [(4, 1)],
  [],
  [(4, 5)]
]
v = len(graph)
dist = [math.inf] * v # O(V)

def Dijkstra(start):
  # Init dist / heap / heap with start
  dist[start] = 0
  hq = [(0, start)]

  while hq:
    # pop current shortest distance node
    d, cur = heapq.heappop(hq) 
    if d > dist[cur]: continue # pass decided node
      
    for next, weight in graph[cur]: 
      new_dist = dist[cur] + weight
      if new_dist < dist[next]:
        dist[next] = new_dist
        heapq.heappush(hq, (new_dist, next))


Dijkstra(0)

for i in range(v): print("dist[",i,"] = ", dist[i]) # print distance
```
<b> Complexity </b>
* Time : O(V + ElgV)
* Space : O(V)

# 문제
## 리트코드
**743. Network Delay Time**
[Network Delay Time - LeetCode](https://leetcode.com/problems/network-delay-time/)

## 프로그래머스

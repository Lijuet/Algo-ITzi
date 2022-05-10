# DFS는 무엇일까?
그래프나 트리 등과 같은 자료구조를 탐색 또는 검색하는 알고리즘이다. 이 알고리즘은 시작 노드부터 backtracing 하기 전까지 최대한 깊이 들어간다.
1. 시작 노드를 스택에 삽입하고 방문처리한다.
2. 스택이 빈 상태가 될까지 다음을 반복한다.
    1. 스택의 최상단 노드를 꺼낸 후 방문처리한다.
    2. 현 노드에서 방문하지 않은 인접한 노드 한개라도 있으면 그 노드를 스택에 넣는다.

# 주의할 점
DFS로 풀까 착각하기 쉬운 유형은 Dijkstra이다. (주관적 경험...)
DFS로 한번 돌았던 경로를 한번 더 돌아야하는 경우가 있다.
이런 경우
1. 노드별로 visited도 같이 스택에 저장시키면 되지만, 이런 경우 현재 파고들고 있는 경로에만 visited가 의미가 있고 backtracing해서 새로운 경로를 파고들게 되는 경우 전 visited는 의미가 없어진다. 예전에 탐색했던 부분 경로를 또 탐색해야 한다. 즉, 시간 초과 가능성 있음. 물론 DP를 써도 되지만...!
2. 아님 Dijkstra를 고려해보자

# 구현 방법
DFS를 Iteration을 이용 할 수도 있고, Recurstion을 이용 할 수도 있다.
구현하기 편한건 개인적으로 Recursion이지만, 함수 호출 횟수가 늘어나면서 시간 초과/너무 많은 함수 호출로 답이 틀려서 주로 최대한 Iteration을 이용한다. (테스트 케이스 크기가 크다면..)

## 방법 1 : Recursion
```
# 재귀 함출시 길이 제한이 있다!! 주의하거나 늘려주거나
graph = [
	[1, 3],
	[3, 4],
	[2, 5],
  [0, 2],
  [],
  []
]
V = len(graph)
def DFS_recur(graph, node, visited):
  visited[node] = True
  print(node, end=" ")

  for next in graph[node]:
    if not visited[next]: 
      DFS_recur(graph, next, visited)

visited = [False] * V
start = time.time()
DFS_recur(graph, 0, visited)
print()
end = time.time() 
print(f"{end - start:.5f} sec")

'''
0 1 3 2 5 4 
0.00009 sec
'''
```

## 방법 2 : Iteration
```
graph = [
	[1, 3],
	[3, 4],
	[2, 5],
  [0, 2],
  [],
  []
]
v = len(graph)

def DFS_iter(graph, start):
  st = [start]
  visited[start] = True
  
  while st:
    cur = st.pop()
    print(cur, end=" ")
    visited[cur] = True

    for next in graph[cur]:
      if not visited[next]:
        st.append(next)

visited = [False] * V
start = time.time()
DFS_iter(graph, 0)
print()
end = time.time() 
print(f"{end - start:.5f} sec")

'''
0 3 2 5 1 4 
0.00004 sec
'''

```

# Complexity
* Time : O(V+E)
* Space  : O(V)

# Advanced
## Handling Disconnected Graph
그래프가 연결이 되어 있지 않아도 한 노드에 대해서 DFS를 돌고 visit 하지 않은 노드에 대해서 다시 DFS를 돌면 된다.
```
for i in range(v):
    if not visited[i]: DFS(i)
```

## Cycle Detection

## Topological Sorting
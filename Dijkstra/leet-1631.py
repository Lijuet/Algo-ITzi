from math import inf
import heapq

def minimumEffortPath(heights):
    hq = [(0, 1, 1)]
    rl, cl = len(heights[0]), len(heights)
    cost = [[inf] * (rl + 2) for _ in range(cl + 2)]
    cost[1][1] = 0
    
    nb = [[-1] * (rl + 2) for _ in range(cl + 2)]
    for i in range(1, cl + 1):
        for j in range(1, rl + 1):
            nb[i][j] = heights[i - 1][j - 1]
            
    while hq:
        c, x, y = heapq.heappop(hq)
        if cost[x][y] < c: continue
        
        for nx, ny in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
            if nb[nx][ny] != -1 and (nc := max(abs(nb[nx][ny] - nb[x][y]), c)) < cost[nx][ny]:
                cost[nx][ny] = nc
                heapq.heappush(hq, (nc, nx, ny))
        
    return cost[cl][rl]

heights = [[1,10,6,7,9,10,4,9]]
print(minimumEffortPath(heights=heights))
from math import inf
from itertools import permutations, product
from collections import deque
from copy import deepcopy

def solution(board, r, c):
    def calDist(sx, sy, n, tboard):
        nt, ni = n
        next = card[nt][ni]
        q = deque([[sx, sy, 0]])
        visited = [[False for j in range(size)] for i in range(size)]
        visited[sx][sy] = True
        
        while q:
            x, y, d = q.popleft()
            print(f"\tcur {x, y} with {d}\t{q} & {tboard[3][2]}")
            
            if (x, y) == next: 
                tboard[x][y] = 0
                return d
            
            # move
            for nx in range(x + 1, size):
                if nx < size and not visited[nx][y]:
                    if nx == x + 1:
                        visited[nx][y] = True
                        q.append((nx, y, d+1))
                        if tboard[nx][y] != 0: break
                    elif tboard[nx][y] != 0 or nx == size - 1:
                        visited[nx][y] = True
                        q.append((nx, y, d+1))
                        break
            for nx in range(x - 1, -1, -1):
                if -1 < nx and not visited[nx][y]:
                    if nx == x - 1:
                        visited[nx][y] = True
                        q.append((nx, y, d+1))
                        if tboard[nx][y] != 0: break
                    elif tboard[nx][y] != 0 or nx == 0:
                        visited[nx][y] = True
                        q.append((nx, y, d+1))
                        break
            for ny in range(y + 1, size):
                if ny < size and not visited[x][ny]:
                    if ny == y + 1:
                        visited[x][ny] = True
                        q.append((x, ny, d+1))
                        if tboard[x][ny] != 0: break
                    elif tboard[x][ny] != 0 or ny == size - 1:
                        visited[x][ny] = True
                        q.append((x, ny, d+1))
                        break
            for ny in range(y - 1, -1, -1):
                if -1 < ny and not visited[x][ny]:
                    if ny == y - 1:
                        visited[x][ny] = True
                        q.append((x, ny, d+1))
                        if tboard[x][ny] != 0: break
                    elif tboard[x][ny] != 0 or ny == 0:
                        visited[x][ny] = True
                        q.append((x, ny, d+1))
                        break
        return 0
            
    size = 4
    cord = [(i,j) for i in range(size) for j in range(size)]
    
    # Find Card Set
    card = {}
    for x, y in cord:
        if (character := board[x][y]) != 0:
            if character not in card: card[character] = []
            card[character].append((x, y))
    print(card)
    
    # Make Order
    order = set()
    for o in set(product(*[[(k,0), (k,1)] for k in card.keys()])): order.update((permutations(o)))
    order = sorted(list(order))
    
    minNum = inf
    for o in order:
        sx, sy = r, c
        tboard = cdeepcopyopy(board)
        temp = 0
        print(f"{o}")
        for nt, ni in o:
            print(f"cur is {sx, sy} and next is {card[nt][ni - 1]} and temp {temp}")
            temp += (cost := calDist(sx, sy, (nt, ni), tboard))
            sx, sy = card[nt][ni]
            
            ni = 0 if ni == 1 else 1
            temp += (cost := calDist(sx, sy, (nt, ni), tboard))
            sx, sy = card[nt][ni]
            
            temp += 2
        if temp < minNum: minNum = temp
    return minNum

board = [[1, 0, 0, 3], [2, 0, 0, 0], [0, 0, 0, 2], [3, 0, 1, 0]]
r = 1
c = 0
print(solution(board, r, c))
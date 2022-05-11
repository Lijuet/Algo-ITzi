def fillSnail1(N, M):
    arr = [[0] * M for _ in range(N)]
    row, col, cnt = 0, -1, 0
    col_num, row_num = M, N
    step = 1

    while col_num and row_num:
        for _ in range(col_num):
            cnt += 1
            col += step
            arr[row][col] = cnt
        
        row_num -= 1
        for _ in range(row_num):
            cnt += 1
            row += step
            arr[row][col] = cnt
        
        col_num -= 1
        step *= -1
    
    for a in arr:
        for j in a: print(j, end='\t')
        print()

def fillSnail2(N, M):
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    arr = [[0] * M for _ in range(N)]
    x, y, di = 0, 0, 0

    for cnt in range(1, N * M + 1):
        arr[x][y] = cnt
        x, y = x + dirs[di][0], y + dirs[di][1]

        if x < 0 or x >= N or y < 0 or y >= M or arr[x][y]: # size를 초과했거나 이미 채웠거나!
            x, y = x - dirs[di][0], y - dirs[di][1]
            di = (di + 1) % 4
            x, y = x + dirs[di][0], y + dirs[di][1]

    for a in arr:
        for j in a: print(j, end='\t')
        print()
            

N, M = 5, 7
fillSnail1(N, M)
print()
fillSnail2(N, M)
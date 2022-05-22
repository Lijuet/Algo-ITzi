'''
LINK : [연습 문제 > 행렬의 곱셈](https://programmers.co.kr/learn/courses/30/lessons/12949?language=python3)
'''
def solution(arr1, arr2):
    m, n, l = len(arr1), len(arr1[0]), len(arr2[0])
    answer = [[0] * l for _ in range(m)]
    for i in range(m):
        for j in range(l):
            val = 0
            for k in range(n):
                val += arr1[i][k] * arr2[k][j]
            answer[i][j] = val
    return answer
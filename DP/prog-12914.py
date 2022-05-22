'''
LINK : [연습문제>멀리 뛰기](https://programmers.co.kr/learn/courses/30/lessons/12914)
11부터 런타임에러
'''
from collections import deque

def solution(n):
    def DP(x, xlist):
        if x == n: return 1
        if x > n: return 0
    
        k = tuple(xlist)
        
        if k not in dp: dp[k] = DP(x + 1, (k[0] + 1, k[1])) + DP(x + 2, (k[0], k[1] + 1))
        return dp[k]
    
    dp = {}
    answer = DP(0, (0, 0))
    return answer % 1234567

n = 1000
print(solution(n))
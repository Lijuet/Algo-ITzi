'''
LINK : [2020 KAKAO BLIND RECRUITMENT > 문자열 압축](https://programmers.co.kr/learn/courses/30/lessons/60057)
OPINION : 
모든 케이스 확인
'''

from math import ceil
def solution(s):
    answer = 0
    sl = len(s)
    
    for l in range(1, sl // 2 + 1):
        pre = s[:l]
        wcnt, tcnt = 1, 0
        for i in range(1, ceil(sl / l) + 1):
            cur = s[l * i:min(l * (i + 1), sl)] if l * i < sl else None
            if cur == pre:  wcnt += 1
            else:
                tcnt += len(pre) + (len(str(wcnt)) if wcnt != 1 else 0)
                wcnt = 1
            pre = cur
        if tcnt > answer : answer = tcnt
    
    return answer

s = "aabbaccc"
print(solution(s))
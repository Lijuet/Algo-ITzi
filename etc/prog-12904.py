'''
LINK: [연습문제>가장 긴 팰린드롬](https://programmers.co.kr/learn/courses/30/lessons/12904?language=python3)
'''
def solution(s):
    answer = 0
    maxLen = 0
    for l in range(len(s), 0, -1):
        for si in range(0, len(s) - l + 1):
            ss = s[si:si+l]
            if ss == ss[::-1]: return l
'''
LINK : [2156. Find Substring With Given Hash Value](https://leetcode.com/problems/find-substring-with-given-hash-value/)
OPINION : 
롤링해쉬를 이용해 스트링 매치를 하는 Rabin-Karp 알고리즘 문제이다.
모듈러 연산은 나누기가 어렵기 때문에 최대한 곱하기 더하기 빼기에서 해결하는 것이 좋다.
O(N^2)으로 걸릴뻔한 스트링 매칭을 O(N)으로 바뀐다
'''
from collections import Counter
class Solution:
    def subStrHash(self, s: str, p: int, m: int, k: int, hashValue: int) -> str:
        alpa2num = {c: ord(c) - 96 for c in Counter(s)}
        i = len(s) - k
        pkm = pow(p, k - 1, m)
        tempHash = sum([alpa2num[s[len(s) - i]] * pow(p, k - i, m) % m for i in range(1, k + 1)]) % m
        
        for idx in range(len(s) - k - 1, -1, -1):
            bef, aft = s[idx + k], s[idx]
            tempHash = (tempHash - alpa2num[bef] * pkm) % m
            tempHash = (tempHash * p % m) % m
            tempHash = (tempHash + alpa2num[aft] % m) % m
            if tempHash == hashValue: i = idx
        return s[i:i+k]
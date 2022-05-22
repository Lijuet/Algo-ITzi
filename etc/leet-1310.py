'''
LINK : [1310. XOR Queries of a Subarray](https://leetcode.com/problems/xor-queries-of-a-subarray/)
OPINION : 
XOR와 부분합을 이용했다.
'''
class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        for i in range(1, len(arr)): arr[i] ^= arr[i - 1]
        return [arr[ei]^arr[si  - 1] if si > 0 else arr[ei] for si, ei in queries]
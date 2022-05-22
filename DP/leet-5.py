'''
LINK : [Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/)
OPINION : 
DP Bottom Up 방식 사용했다. 16번째 줄에 start가 증가하면 dp를 적용할 수 없다. 감소하는 방식으로 해야 dp[start + 1][end - 1]가 셋팅되어있다.


'''
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        maxs, maxl = 0,  1
        dp  = [[False] * n for _ in range(n)]
        
        for i in range(n): dp[i][i] = True
        
        for start in range(n - 1, -1, -1):
            for end in range(start + 1, n):
                if s[start] == s[end]:
                    if end - start == 1 or dp[start + 1][end - 1]:
                        dp[start][end] = True
                        l = end - start + 1
                        if maxl < l:
                            maxl = l
                            maxs = start
                
        return s[maxs:maxs + maxl]

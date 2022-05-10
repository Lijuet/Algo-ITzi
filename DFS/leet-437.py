'''
LINK : [Path Sum III](https://leetcode.com/problems/path-sum-iii/submissions/)
OPINION
처음에 투포인터 썼다가 음의 값이 있으면 투포인터가 소용이 없음을 깨달음
DFS로 다시 시도함. 이는 [해당 사이트](https://zhenyu0519.github.io/2020/03/16/lc437/)를 참고했음.
뭔가 DFS를 두번 사용한게 신기했음.
'''

from collections import deque
import copy

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def DFS(root, sum):
            answer = 0
            if not root: return answer
            if sum == targetSum: answer += 1
            
            if root.left: answer += DFS(root.left, sum + root.left.val)
            if root.right: answer += DFS(root.right, sum + root.right.val)
                
            return answer
        if not root: return 0
        return DFS(root, root.val if root else 0) + self.pathSum(root.left, targetSum) + self.pathSum(root.right, targetSum)
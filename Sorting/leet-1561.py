'''
LINK : [1561. Maximum Number of Coins You Can Get](https://leetcode.com/problems/maximum-number-of-coins-you-can-get/)
OPINION : 
내가 x라는 값을 줄려면 적어도 엘리스에게틑 x+1값을 줘야한다. 
그 상태에서 내가 최대한 높은 숫자의 x를 가지려면 Bob에게 돌아가는 숫자를 최대한 줄인다.
즉, 내림차순으로 소팅한 후 2의 배수 자리 숫자를 n(piles.length / 3)개 가져가면된다.
밥은 그냥 제일 작은 숫자를 가져간다
'''


class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        return sum([piles[2 * i + 1] for i in range(len(piles) // 3)])
'''
LINK : [Summer/Winter Coding > 스티커 모으기 2](https://programmers.co.kr/learn/courses/30/lessons/12971)
OPINION : 
dp인데, 처음과 끝이 연결되어 있어 단순한 1차원 dp로 못푼다. 처음 카드를 포함했는냐 마느냐에 따라 다르기때문에 2차원 dp를 활용했다.
못풀어서 아래 사이트 코드를 보고 풀었다.
https://velog.io/@study-dev347/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%8A%A4%ED%8B%B0%EC%BB%A4-%EB%AA%A8%EC%9C%BC%EA%B8%B02

'''

def solution(sticker):
    answer = 0
    sl = len(sticker)
    if sl == 1: return sticker[0]
    dp = [[0] * sl for _ in range(2)]
    
    dp[0][1] = sticker[1]
    dp[1][0] = sticker[0]
    dp[1][1] = sticker[0]
    
    for i in range(2, sl): dp[0][i] = max(dp[0][i - 1], dp[0][i - 2] + sticker[i])
    for i in range(2, sl - 1): dp[1][i] = max(dp[1][i - 1], dp[1][i - 2] + sticker[i])
    
    return max(dp[0][sl - 1], dp[1][sl - 2])

sticker = [14, 6, 5, 11, 3, 9, 2, 10]
print(solution(sticker))
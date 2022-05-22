'''
LINK : [월간 > 110 옮기기](https://programmers.co.kr/learn/courses/30/lessons/77886)
OPINION :
'''
def solution(nums):
    answer = []    
    for ss in nums:
        repeat = True
        st = []
        cnt_110 = 0
        for s in ss:
            if len(st) >= 2 and st[-1] == '1' and st[-2] == '1' and s == '0':
                cnt_110 += 1
                st.pop()
                st.pop()
            else:
                st.append(s)

        cnt_1 = 0
        for s in st[::-1]:
            if s == '1': 
                cnt_1 += 1
            else: break
        answer.append(''.join(st[:len(st) - cnt_1]) + '110' * cnt_110 + '1' * cnt_1)
    return answer
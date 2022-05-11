'''
LINK : 2195. Append K Integers With Minimal Sum[https://leetcode.com/problems/append-k-integers-with-minimal-sum/]
OPINION : 
매우 큰 수(100,000,000)만큼 arr 선언했던 코드가 메모리 초과가 났다. 
100만개 이상 선언하게 될거 같으면 다른 알고리즘을 찾아보자.
이번에는 연속합을 구하는 부분이 있어서 공식으로 대체했다.
'''
def minimalKSum(nums, k):
    def sumFromTo(a, b):
            return int((b + a - 1) * (b - a) / 2)

    nums.sort()
    start = 1
    result = 0
    
    for end in nums:
        if start > end: continue
        temp = sumFromTo(start, min(end, start + k))
        k -= (min(end, start + k) - start)
        result += temp
        start = end + 1
        if not k: break
                
            
    if k: result += [i for i in range(nums[-1] + 1, nums[-1] + 1 + k)]
        
    return sum(result)


nums = [96,44,99,25,61,84,88,18,19,33,60,86,52,19,32,47,35,50,94,17,29,98,22,21,72,100,40,84]
k = 35
print(minimalKSum(nums, k))
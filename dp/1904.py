n = int(input())

dp = [0, 1, 2]
dp[1] = 1
dp[2] = 2 # 이렇게 미리 정의해두면 n=1일때 ,,문제생김. append로 해보기
for i in range(3, n+1):
    dp.append((dp[i-1]+dp[i-2])% 15746)
print(dp[n])
"""
    [0] * n 방식
•	장점: 메모리 크기가 처음부터 고정돼서 인덱스 접근이 빠름. 이렇게 해두 ㄱㅊ.
•	단점: 그치만 !!!!!!! n 값이 1이나 2 같은 작은 경우, 인덱스 범위 관리 필요. 예외처리 필수~~

"""


## 파이썬은 매우 큰 수를 처리할 수는 있지만 그만큼 메모리 사용량이 많아진다!

# 재귀로 풀엇더니 메모리초과, 시간초과가 발생 ㅠ..ㅠ

# import sys
# sys.setrecursionlimit(10**6)

# def sol(n):
#     if n==0:
#         return 1
#     elif n<0:
#         return 0
    
#     if memo[n] != 0 :
#         return memo[n]
#     else:
#         ans = (sol(n-1) + sol(n-2))%15746
#         memo[n] = ans
#         return memo[n]

# n = int(input())
# memo = [0] * (n+1)
# print(sol(n)%15746)
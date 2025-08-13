import sys
sys.setrecursionlimit(10**6)

def fibbo(n):
    if n<=2:
        return 1
    if memo[n] != 0:
        return memo[n]
    else:
        memo[n] = (fibbo(n-1) + fibbo(n-2))%1000000007
        return memo[n]

n = int(input())

memo = [0]*(n+1)

memo[1] = 1
memo[1] = 2
print(fibbo(n)%1000000007)

"""
수 자체가 넘 크면 그럴 수 있음. 
나머지를 계속 해야할듯
"""
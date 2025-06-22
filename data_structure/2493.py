n = int(input())
arr = list(map(int, input().split()))

stack = []

'''
가장 가까운 큰게 필요함
그럼 전꺼 포문 돌아야함 근데너무비효율적임
-> 나보다 큰거만 담아두는 자료구조를 둔다
-> 그 스택만보면서 큰애들만잇으니까 그거보고 레이저 맞을 첫번째 애 판단 가능
스택에서 답을 고른당
'''

for i, x in enumerate(arr):
    while stack and stack[-1][1] < x:
        stack.pop()
    if not stack:
        print(0, end=' ')
    else:
        print(stack[-1][0]+1, end=' ')
    stack.append((i, x))
n = int(input())
arr = list(map(int, input().split()))

stack = []
result = [-1] * n


for i, x in enumerate(arr):
    while stack and stack[-1][1] < x:
        a, b = stack.pop()
        result[a] = x
    stack.append((i, x))


print(*result)

'''
가장 오른쪽에서 가까운 큰 수 
걍 아직 할당안된 왼쪽에잇는 수면 무조건 내가 오큰수
내숫자보고 오른쪽꺼 스택에 넣고하는게 쉽지않음 그럼 반대로 생각해보기
스택에 두고 
2 1 6 5 3 4

나보다 작으면 무조건 할당해주면됨
무조건 스택은 내림차순

6 5


'''
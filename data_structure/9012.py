n = int(input())

for _ in range(n):
    lst = list(input())
    stack = []
    result = "YES"
    for l in lst:
        if l == "(":
            stack.append(0)
        elif l == ")":
            if stack:
                stack.pop()
            else:
                result = "NO"
                break
    if stack:
        result = "NO"
    print(result)
    
    """
    헐~ ()를 공백으로 대체하면 됏엇슴... 어이엄다
    파이썬 for else? break나오면안걸리는건가바
    for : else: -> break하고 안걸렷을때 실행됨
    """
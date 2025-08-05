n = int(input())
arr = [int(input()) for _ in range(n)]

last_num = 1
prev = [i for i in range(n, 0, -1)]
stack = []

result = []
NO = False

idx = 0

last_num = 1
for num in arr:
    # 스택 쌓기
    while last_num <= num:
        stack.append(last_num)
        last_num += 1
        result.append("+")
    if stack and stack[-1] == num:
        stack.pop()
        result.append("-")
    else:
        print("NO")
        exit()



print("\n".join(result))
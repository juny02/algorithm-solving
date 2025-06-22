n = int(input())

arr = [int(input()) for _ in range(n)]
result = []
last_num = 1
stack = []
for x in arr:
    while last_num <= x:
        stack.append(last_num)
        result.append("+")
        last_num += 1
    while True:
        if not stack or stack[-1] < x:
            print("NO")
            exit()
        else:
            result.append("-")
            if x == stack.pop():
                break

print(result)

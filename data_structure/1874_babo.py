n = int(input())
arr = [int(input()) for _ in range(n)]

last_num = 1
prev = [i for i in range(n, 0, -1)]
stack = []

result = []
NO = False

for num in arr:
    while True:
        if len(stack) == 0 or stack[-1] < num:
            if prev:
                add_num = prev.pop()
                if add_num > num:
                    NO = True
                    break
                else:
                    stack.append(add_num)
                    result.append("+")
            else:
                NO = True
                break
        elif stack[-1] == num:
            stack.pop()
            result.append("-")
            break
        elif stack[-1] > num:
            stack.pop()
            result.append("-")
    if NO:
        print("NO")
        exit()
for i in result:
    print(i)


left = list(input())
right = []

n = int(input())


for _ in range(n):
    cmd = input().split()
    if cmd[0] == "L":
        if left: right.append(left.pop())
    elif cmd[0] == "D":
        if right: left.append(right.pop())
    elif cmd[0] == "B":
        if left: left.pop()
    elif cmd[0] == "P":
        left.append(cmd[1])

print(*left, sep='', end='')
print(*right[::-1], sep='')


"""
커서를 기준으로 상태! 변화가 일어남
-> 커서 기준으로 양옆을 나눠 관리하면됨
커서 바로 앞/뒤 부분만 변화가 발생하므로 스택으로 관리하면됨 거기서 떨어져서 변화가 생기지 않으므로

!! 오른쪽꺼는 스택이니까 거꾸로 출력해줘야함!!
"""
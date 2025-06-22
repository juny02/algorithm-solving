import sys
from collections import deque

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    p = input()
    n = int(input())
    s = input()[1:-2]
    arr = list(map(int,s.split(','))) if s else []
    queue = deque(arr)
    error = False
    r_flag = False

    for cal in p:
        if cal == "R":
            r_flag = not r_flag
        elif cal == "D":
            if queue:
                if r_flag:
                    queue.pop()
                else:
                    queue.popleft()
            else:
                error = True
                break
    if error:
        print("error")
    else:
        if r_flag:
            queue.reverse()
        print(f"[{','.join(map(str, queue))}]")

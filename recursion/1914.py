n = int(input())


def hanoi(n: int):
    if n == 1:
        return 1
    else:
        return 2 * hanoi(n - 1) + 1

process = []

def hanoi_process(n: int, start: int, end: int, left: int):
    if n==1:
        print(f"{start} {end}")
    else:
        hanoi_process(n-1, start, left, end)
        hanoi_process(1, start, end, left)
        hanoi_process(n-1, left, end, start)
    

    """
    중간꺼를 담는게 핵심 아이디어 ~~~
    """


print(hanoi(n))
if n <= 20:
    hanoi_process(n, 1, 3, 2)
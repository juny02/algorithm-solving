
# in연산이니까 set!!!!!!!!
"""
- 빈칸을 배열에 담아두는 식으로 함 . 근데 메모리초과가 뜸 (pypy3에서는 안뜸)
다른 방법이 머가잇지?
"""

def square(n):
    if n == 3:
        return {(1,1)}
    else:
        gap = n//3

        blanks = square(n//3)
        result = set()
        for x, y in list(blanks):
            for k in range(0, 3):
                for i in range(0, 3):
                    result.add((x + k*gap, y + i*gap))
                    
        for i in range(gap, gap*2):
            for j in range(gap, gap*2):
                result.add((i, j))
    
        return result


def print_square(n):
    blanks = square(n)
    for i in range(n):
        for j in range(n):
            if (i, j) in blanks:
                print(" ", end='')
            else:
                print("*", end='')
        print()
n = int(input())

print_square(n)
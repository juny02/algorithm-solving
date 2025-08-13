
def build(n):
    if n==3:
        return ["***", "* *", "***"]
    else:
        sub = build(n//3)
        top = []
        
        # 곱셈 말고 더하게 연산!! 문자열더하기연산!
        top = [s+s+s for s in sub]
        blank = n//3*" "
        middle = [s+blank+s for s in sub]
        return top+middle+top

n = int(input())
print('\n'.join(build(n)))
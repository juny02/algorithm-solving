n = int(input())
arr = list(input())
nums = {}
for i in range(n):
    nums[chr(65+i)] = int(input())

stack = []
result = 0
for char in arr:
    if 'A' <= char <= 'Z':
        stack.append(nums[char])
    else:
        a = stack.pop()
        b = stack.pop()
        
        if char == "*":
            stack.append(b*a)
        elif char == "+":
            stack.append(b+a)
        elif char == "-":
            stack.append(b-a)
        elif char == "/":
            stack.append(b/a)
            
print(f"{stack.pop():.2f}")


n, k = map(int, input().split())
nums = list(map(int, (list(input()))))

stack = []
count = 0
for i, num in enumerate(nums):
    while stack and stack[-1] < num and count < k:
        stack.pop()
        count += 1
    stack.append(num)

# 일단 다 넣구 후처리해도 됨
if count < k:
    stack=stack[:-(k-count)]


print("".join(map(str, stack)))

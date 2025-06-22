n, k = map(int, input().split())
nums = list(map(int, (list(input()))))

stack = []
count = 0
for i, num in enumerate(nums):
    while stack and stack[-1] < num and count < k:
        stack.pop()
        count += 1
    # print(f"=====NUM {num}=====")
    # print(f"count {count}")
    # print(f"stack {stack}")
    # print(f"n-k {n - k}")
    # print(f"k-count {k-count}")
    # print(f"(n-i)+1{(n-i)+1}")
    # print(f"i {i}")
    if k - count == (n - i) and len(stack) == n - k:
        count += 1
        continue
    stack.append(num)
    # print(f"stack {stack}")


print("".join(map(str, stack)))

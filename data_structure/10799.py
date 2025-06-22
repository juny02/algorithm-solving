arr = input()
arr = arr.replace("()", "0")

stack = []
count = 0
for x in arr:
    if x == "(":
        stack.append(1)
    elif x == ")":
        stack.pop()
        count += 1
    elif x == "0":
        count += len(stack)

print(count)

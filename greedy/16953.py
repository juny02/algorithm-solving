a, b = map(int, input().split())

# def get_n(count, num):

#     if num == a:
#         print(count+1)
#         exit()
#     if num < a:
#         print(-1)
#         exit()

#     if num % 10 == 1:
#         get_n(count+1, int(num/10))
#     elif num % 2 == 0:
#         get_n(count+1, int(num/2))
#     else:
#         print(-1)
#         exit()

# get_n(0, b)

# 반복문
count = 0
while a != b:
    if a > b:
        count = -2
        break
    elif b % 10 == 1:
        b = b // 10
        count += 1
    elif b % 2 == 0:
        b = b // 2
        count += 1
    else:
        count = -2
        break
print(count + 1)

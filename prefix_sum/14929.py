import copy

N = int(input())
arr = list(map(int, input().split()))
sum_arr = copy.deepcopy(arr)

for i in range(N - 2, 0, -1):
    sum_arr[i] += sum_arr[i + 1]

answer = 0
for i in range(0, N - 1):
    answer += arr[i] * sum_arr[i + 1]

print(answer)

N, M = map(int, input().split())
arr = list(map(int, input().split()))
sum_arr = [arr[0]] # 누적합은 첫번째꺼 미리 넣어놓는담

for i in range(1, N):
    sum_arr.append(arr[i]+sum_arr[i-1])

for _ in range(M):
    i, j = map(int, input().split())
    prev_sum = sum_arr[i-2] if i-1>0 else 0
    print(sum_arr[j-1]-prev_sum)


# for _ in range(M):
#     i, j = map(int, input().split())
#     print(sum_arr(i, j, arr))

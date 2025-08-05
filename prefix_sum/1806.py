N, S = map(int, input().split())
arr = list(map(int, input().split()))

arr_sum = [arr[0]]

for i in range(1, N):
    arr_sum.append(arr_sum[i - 1] + arr[i])

print(arr_sum)

i, j = 0, 0
min_val = float("inf")
candidates = []
while i < j:
    temp = arr_sum[j] - arr[i]

    if temp > 15:
        i += 1
    elif temp < 15:
        

"""
합이 S인 것 중 가장 짧은 부분합 구하기
연속된 수 중에서 !!

이제 배열의 두 요소의 차가 특정값이랑 가장 비슷해질때를 찾아야함
100,000의조합...?
"""

N = int(input())
arr = list(map(int, input().split()))
arr.sort()

i, j = 0, len(arr)-1
min_val = float('inf')
min_i, min_j = 0, 0
while i < j:
    temp = arr[i] + arr[j]
    if abs(temp) < abs(min_val):
        min_val=temp
        min_i, min_j = i, j
    if temp < 0:
        i += 1
    elif temp > 0:
        j -= 1
    else:
        print(f"{arr[i]} {arr[j]}")
        exit()

print(f"{arr[min_i]} {arr[min_j]}")
        


"""
- 9 -8      7 11

음수면 i 이동
0보다 작으면 - 더 늘려야하니까 큰수로

양수면 j이동?
0보다 크면 더 줄여야하므로 작은수로

어느쪽이든 둘다 0 을 향해서 간다!!

min은 계속 갱신하면서 가는거고 이동은 간단하게 한칸씩!!

"""

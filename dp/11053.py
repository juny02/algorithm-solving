n = int(input())
arr = list(map(int, input().split()))

count = [1]*n # 첨에 걍 다 1로 초기화하고 

for i, num in enumerate(arr):
    candidates = [1]
    # print(f"i: {i}, num: {num}")
    # print(count[:i])
    for c_idx, c_num in enumerate(count[:i]): #그럼 굳이 1이면 안돌아도 되니깐!
        if num > arr[c_idx]:
            count[i] = max(count[c_idx]+1, count[i]) # 원래 가지고 잇던 값이랑 새로 가져온거중에 최대인걸로
print(max(count))

"""
DP배열을 따로 두고 재사용하는거
"""
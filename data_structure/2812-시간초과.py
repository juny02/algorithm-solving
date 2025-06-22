n, k = map(int, input().split())
nums = list(input())
candidate = nums[: -(k - 1)]

"""
k가 들어오면
k-1 숫자뺀 곳에서 젤 큰거


"""
left = n - k

answer = []
while len(answer) < n - k:
    # print(f"candidate: {candidate}")
    max_num, max_idx = max((v, i) for i, v in enumerate(candidate))
    answer.append(max(candidate))
    # print(f"answer: {answer}")
    left -= 1
    if left - 1 > 0:
        candidate = nums[max_idx + 1 : -(left - 1)]
    else:
        candidate = nums[max_idx + 1 :]

print(''.join(answer))

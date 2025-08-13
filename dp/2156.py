N = int(input())

arr = [int(input()) for _ in range(N)]

dp = [0, arr[0], arr[0]]

for i in range(1, N):
    # print(dp)
    a, b, c = dp
    dp[0] = max(a,b,c) # 이걸 생각 못해냄.. 지피띠니가 알려줌
    dp[1] = a+arr[i]
    dp[2] = b+arr[i]
    
print(max(dp))


    # # 직전꺼 검사
    # print(f"!!!!!!!!{i}")
    # if prev_nums[i-1] < 2:
    #     dp[i] = dp[i-1]+arr[i]
    #     prev_nums[i] = prev_nums[i-1]+1
    
    # for j in range(i-1):
    #     print(j)
    #     print(dp[j])
    #     print(arr[i])
    #     print(dp[j]+arr[i])
    #     if dp[i] <= dp[j]+arr[i]:
    #         dp[i] = dp[j]+arr[i]
    #         prev_nums[i] = 1
        

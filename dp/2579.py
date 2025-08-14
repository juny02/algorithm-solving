N = int(input())
data = [0] # 1부터 하려면 그래서 직관적이게하려면 첨에 하나 채우고 시작~
for _ in range(N):
    data.append(int(input()))
# dp[i] = i칸을 꼭 지날때의 최대

if N==1:
    print(data[1])
elif N==2:
    print(data[1]+data[2])
else:
    dp = [0, data[1], data[1]+data[2]]
    for i in range(3, N):
        dp.append(max(dp[i-2]+data[i], dp[i-3]+data[i]+data[i-1]))
    print(dp[-1])
N,M = map(int,input().split())
A = list(map(int,input().split()))

#dp = [[0]*(W+10)]*(N+10)
dp = [[0 for j in range(M+10)]for i in range(N+10)]
dp[0][0] = 1
"""
for i in range(N+10):
    dp[i][0] = 1
"""
for i in range(N):
    for m in range(M+1):
        if m >= A[i]:
            dp[i+1][m] = (dp[i][m] + dp[i][m-A[i]])%1000
        else:
            dp[i+1][m] = dp[i][m]%1000
"""
for i in range(N+1):
    print(dp[i])
"""
print(dp[N][M])

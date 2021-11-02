N,M = map(int,input().split())
A = list(map(int,input().split()))
f_inf = float('inf')
#dp = [[0]*(W+10)]*(N+10)
dp = [[ f_inf for j in range(M+10)]for i in range(N+10)]
dp[0][0] = 0
"""
for i in range(N+10):
    dp[i][0] = 1
"""
for i in range(N):
    for m in range(M+1):
        if m >= A[i]:
            dp[i+1][m] = min(dp[i][m-A[i]]+1, dp[i][m])
        else:
            dp[i+1][m] = dp[i][m]
"""
for i in range(N+1):
    print(dp[i])
"""
if dp[N][M] == f_inf:
    print(-1)
else:
    print(dp[N][M])

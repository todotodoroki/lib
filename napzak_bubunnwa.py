N,M = map(int,input().split())
A = list(map(int,input().split()))

#dp = [[0]*(W+10)]*(N+10)
dp = [[False for j in range(M+10)]for i in range(N+10)]
dp[0][0] = True

for i in range(N):
    for m in range(M+1):
        if m >= A[i]:
            dp[i+1][m] = dp[i][m] or dp[i][m-A[i]]
        else:
            dp[i+1][m] = dp[i][m]

for i in range(N):
    print(dp[i][M])

print("Yes" if dp[N][M] else "No")

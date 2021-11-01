N,W = map(int,input().split())
weight = [0]*(N+10)
value = [0]*(N+10)
for i in range(N):
    weight[i], value[i] = map(int,input().split())

#dp = [[0]*(W+10)]*(N+10)
dp = [[0 for j in range(W+10)]for i in range(N+10)]

for i in range(N):
    for w in range(W+1):
        if w >= weight[i]:
            dp[i+1][w] = max(dp[i][w - weight[i]] + value[i], dp[i][w])
        else:
            dp[i+1][w] = dp[i][w]
"""
for i in range(N):
    print(dp[i])
"""
print(dp[N][W])

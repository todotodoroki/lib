N = int(input())
a = [list(map(int, input().split())) for i in range(2)]
ans = 0
for i in range(N):
    ans = max(sum(a[0][:i+1]) + sum(a[1][i:]),ans)
print(ans)

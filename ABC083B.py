N,A,B = map(int,input().split())

out = 0
for i in range(N+1):
    i = str(i)
    wa = 0
    for n in i:
        wa += int(n)
    if A <= wa and wa <= B:
        out += int(i)

print(out)

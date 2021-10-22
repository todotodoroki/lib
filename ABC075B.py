H,W = map(int,input().split())

d = list()
for i in range(H):
    s = list(input())
    d.append(s)

d_out = d
zeros = ['.']*(W+2)

d.insert(0,zeros)
d.append(zeros)

for i in range(1,H+1):
    d[i].insert(0,'.')
    d[i].append('.')

for i in range(1,H+1):
    for j in range(1,W+1):
        count = 0
        if d[i-1][j-1] == '#':
            count += 1
        if d[i][j-1] == '#':
            count += 1
        if d[i+1][j-1] == '#':
            count += 1
        if d[i-1][j] == '#':
            count += 1
        if d[i+1][j] == '#':
            count += 1
        if d[i-1][j+1] == '#':
            count += 1
        if d[i][j+1] == '#':
            count += 1
        if d[i+1][j+1] == '#':
            count += 1

        if d[i][j] == '.':
            d_out[i][j] = count
        else:
            d_out[i][j] = '#'

for i in range(1,H+1):
    for j in range(1,W+1):
        print(d_out[i][j],end='')
    print("\n")

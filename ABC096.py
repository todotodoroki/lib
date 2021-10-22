def padding(list2d, symbol):
    H = len(list2d)
    W = len(list2d[1])
    symbols = [symbol]*(W+2)
    list2d.insert(0,symbols)
    list2d.append(symbols)
    for i in range(1,H+1):
        list2d[i].insert(0,symbol)
        list2d[i].append(symbol)
    return list2d

H,W = map(int,input().split())

m = [list(input()) for i in range(H)]

m = padding(m,'.')

for i in range(1, H+1):
    for j in range(1, W+1):
        if m[i][j] == '#':
            if m[i-1][j] == '.' and m[i][j-1] == '.' and m[i][j+1] == '.' and m[i+1][j] == '.':
                print("No")
                exit()
print("Yes")

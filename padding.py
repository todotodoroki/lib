def padding(list2d, symbol):
    H = len(list2d)
    W = len(list2d[0])
    symbols = [symbol]*(W+2)
    list2d.insert(0,symbols)
    list2d.append(symbols)
    for i in range(1,H+1):
        list2d[i].insert(0,symbol)
        list2d[i].append(symbol)
    return list2d


#test
N = int(input())
#数字
list2d = [list(map(int,input().split())) for i in range(N)]
#文字列
list2d = [list(input()) for i in range(N)]

print(padding(list2d, "#"))

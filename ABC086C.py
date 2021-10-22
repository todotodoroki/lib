N = int(input())
tp = list()
for i in range(N):
    tmp = list(map(int,input().split()))
    tp.append(tmp)


x = tp[0][1]-0
y = tp[0][2]-0
t = tp[0][0]-0
z = t - (x + y)

if z % 2 != 0 or z < 0:
    print("No")
    exit()
for i in range(len(tp)-1):
    x = abs(tp[i+1][1]-tp[i][1])
    y = abs(tp[i+1][2]-tp[i][2])
    t = abs(tp[i+1][0]-tp[i][0])
    z = t - (x + y)
    if z % 2 != 0 or z < 0:
        print("No")
        exit()
print("Yes")

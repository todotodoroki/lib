l = list(map(int,input().split()))
if l[1] < l[2] or l[3] < l[0]:
    print(0)
    exit()

l.sort()
print(l[2] - l[1])

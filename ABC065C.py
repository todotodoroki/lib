N = int(input())

a = [{"next":int(input()),"flag":0} for i in range(N)]
count = 0
pos = 0

while(1):
    next = a[pos]["next"]
    flag = a[pos]["flag"]
    count += 1
    #print(next)
    if next == 2:
        print(count)
        exit()
    if flag == 1:
        print(-1)
        exit()

    a[pos]["flag"] = 1
    pos = next - 1

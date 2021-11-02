N,Q = map(int,input().split())
q = []
back = [None]*(N+1)
front = [None]*(N+1)

for i in range(Q):
    q.append(list(map(int,(input().split()))))
#print(q)

for i in range(Q):
    if q[i][0] == 1:
        x = q[i][1]
        y = q[i][2]
        front[y] = x
        back[x] = y

    if q[i][0] == 2:
        x = q[i][1]
        y = q[i][2]
        front[y] = None
        back[x] = None

    if q[i][0] == 3:
        #print(front)
        ans = []
        x = q[i][1]
        while front[x] != None:
            x = front[x]
        ans = []
        while x != None:
            ans.append(x)
            x = back[x]
        print(len(ans),end=" ")
        for i in ans:
            print(i,end = " ")
        print("")

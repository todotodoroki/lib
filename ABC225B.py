#a,b = map(int,input().split())
N = int(input())

Graph = [[] for i in range(N)]
for i in range(N-1):
    a,b = map(int,input().split())
    Graph[a-1].append(b-1)
    Graph[b-1].append(a-1)

#print(Graph)
for i in range(N):
    if len(Graph[i]) == N-1:
        print("Yes")
        exit()
print("No")

class DFS():
    def __init__(self, N, Graph): #グラフは頂点とつながっている辺にいての2次元
        self.seen = [False]*N
        self.Graph = Graph
        self.first_order = [[] for i in range(N)]
        self.last_order = [[] for i in range(N)]
        self.first_count = 0
        self.last_count = 0

    def dfs(self, v):
        self.first_order[v] = self.first_count
        self.first_count += 1
        self.seen[v] = True
        #print("v:{} seen:{}".format(v,self.seen))
        for next_v in self.Graph[v]:
            if self.seen[next_v]:
                continue
            else:
                self.dfs(next_v)
        self.last_order[v] = self.last_count
        self.last_count += 1

        return self.seen, self.first_order, self.last_order

#辺が与えられる場合の入出力
N,M = map(int,input().split())
Graph = [[] for i in range(N)]
for i in range(M):
    a,b = map(int,input().split())
    Graph[a].append(b)

dfs = DFS(N, Graph)
reach, first, last = dfs.dfs(0)
for i in range(N):
    print("{}: {},{}".format(i,first[i],last[i]))

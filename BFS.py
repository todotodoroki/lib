import queue

class BFS():
    def __init__(self, N, Graph): #グラフは頂点とつながっている辺にいての2次元
        self.dist = [-1]*N #-1は未訪問
        self.que = queue.Queue()
        self.Graph = Graph

    def bfs(self, start):
        self.dist[start] = 0
        self.que.put(0)

        while not self.que.empty():
            v = self.que.get()
            for nv in self.Graph[v]:
                if self.dist[nv] != -1:
                    continue
                self.dist[nv] = self.dist[v] + 1
                self.que.put(nv)

        return self.dist


#辺が与えられる場合の入出力
N,M = map(int,input().split())
Graph = [[] for i in range(N)]
for i in range(M):
    a,b = map(int,input().split())
    Graph[a].append(b)
    #無向の場合
    Graph[b].append(a)
print(Graph)
bfs = BFS(N, Graph)
dist = bfs.bfs(0)
for i in range(N):
    print("{},{}".format(i,dist[i]))

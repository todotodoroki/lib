import queue

class BFS():
    def __init__(self, H, W, sy, sx,Graph): #グラフは頂点とつながっている辺にいての2次元
        self.dist = [[-1]*W for i in range(H)] #-1は未訪問
        self.que = queue.Queue()
        self.Graph = Graph
        self.sy = sy-1
        self.sx = sx-1

    def bfs(self, start):
        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]
        self.dist[self.sy][self.sx] = 0
        self.que.put([self.sy,self.sx])

        while not self.que.empty():
            v = self.que.get()
            #print(v)
            vx = v[1]
            vy = v[0]
            for i in range(4):
                #print("v:{} i:{}".format(v,i))
                nvx = vx + dx[i]
                nvy = vy + dy[i]

                if nvx < 0 or nvx >= W or nvy < 0 or nvy >= H:
                    pass
                elif self.Graph[nvy][nvx] == "#":
                    pass
                elif self.dist[nvy][nvx] != -1:
                    pass

                else:
                    self.dist[nvy][nvx] = self.dist[vy][vx] + 1
                    self.que.put([nvy,nvx])

        return self.dist



H,W = map(int,input().split())
sy,sx = map(int,input().split())
gy,gx = map(int,input().split())

meiro = []
for i in range(H):
    c = list(input())
    meiro.append(c)
#print(meiro)

bfs = BFS(H, W, sy, sx, meiro)
dist = bfs.bfs(0)
"""
for i in range(H):
    print("{},{}".format(i,dist[i]))
"""
print(dist[gy-1][gx-1])

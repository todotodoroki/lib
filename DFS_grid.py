#ATC001A
import sys
sys.setrecursionlimit(500*500) #再起関数の深さ制限1000を解除

class DFS_grid():
    def __init__(self, H, W, Graph): #グラフは頂点とつながっている辺にいての2次元
        self.seen = [[0]*W for i in range(H)]
        self.Graph = Graph
        self.dx = [1, 0, -1, 0]
        self.dy = [0, 1, 0, -1]

    def dfs(self, h, w):
        #print("h:{} w:{}".format(h,w))
        if h < 0 or h >= H or w < 0 or w >= W:
            return
        if self.seen[h][w] == 1:
            return
        if self.Graph[h][w] == "#":
            return
        #if self.Graph[h][w] == "g":
            #print("Yes")
            #exit()
        #print("h:{} w:{}".format(h,w))
        #print(self.seen)
        self.seen[h][w] = 1
        #print("v:{} seen:{}".format(v,self.seen))
        for dir in range(4):
            nh = h + self.dy[dir]
            nw = w + self.dx[dir]
            self.dfs(nh, nw)

        return self.seen

H,W = map(int,input().split())
meiro = []
for i in range(H):
    c = list(input())
    meiro.append(c)
#print(meiro)
for i in range(H):
    for j in range(W):
        if meiro[i][j] == 's':
            sh = i
            sw = j
        if meiro[i][j] == 'g':
            gh = i
            gw = j
#print(sh,sw)
dfs = DFS_grid(H, W, meiro)
result = dfs.dfs(sh, sw)
#print(result)
if result[gh][gw] == True:
    print("Yes")
else:
    print("No")

import numpy as np
N, M = map(int,input().split())
B = []
C = []
for i in range(N):
    bs = list(map(int,input().split()))
    #bs = np.array(bs)
    B.append(bs)
B = np.array(B)
#print(B)
#print(B)
"""
for i in range(N-1):
    if B[i][0] + 7 != B[i+1][0]:
        print("No")
        exit()
"""
if M >= 8:
    print("No")
    exit()

for i in range(M):
    tmp = sum(B[:,i])
    #print("wa",tmp)
    #print("here",i)
    wa1 = int((2*B[0][i] + (N-1)*7)*N)
    if tmp*2 != wa1:
        #print(wa1)
        print("No")
        exit()

for i in range(N):
    tmp = sum(B[i])
    if tmp*2 != int((B[i][0] + B[i][M-1])*M):
        #print(tmp)
        print("No")
        exit()

for i in range(0,M-1):
    if B[0][i] % 7 == 0:
        print("No")
        exit()

print("Yes")

import math
#a,b = map(int,input().split())
s = list(input())

ns = len(set(s))

if ns == 1:
    print(1)
if ns == 2:
    print(3)
if ns == 3:
    print(6)

a,b,x = map(int, input().split())
ans1=0
ans1 = (a-1)//x + 1
ans2 = b//x + 1
print(ans2-ans1)

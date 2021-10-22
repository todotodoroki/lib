N = int(input())
ai = list(map(int,input().split()))
ai.sort(reverse=True)

Alice=0
Bob=0
#print(ai)
for i,num in enumerate(ai):
    if i%2 == 0:
        Alice += num
    else:
        Bob += num
#print(Alice)
#print(Bob)

print(Alice - Bob)

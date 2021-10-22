N = input()
Ai = list(map(int,input().split()))
count = 0
while(1):
    A_even = [i for i in Ai if i%2 == 0]
    if len(Ai) != len(A_even):
        print(count)
        exit()
    Ai = [i/2 for i in A_even ]
    count += 1

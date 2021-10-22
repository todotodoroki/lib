N = int(input())
we = input()
w = []
e = []
for i in range(len(we)):
    if we[i] == 'W':
        w.append(1)
        e.append(0)
    else:
        e.append(1)
        w.append(0)
#print("w",w)
#print("e",e)
#累積和を計算
w_wa = list([0])
for i in range(len(w)):
    w_wa.append(w_wa[i] + w[i])
#print("w_wa:",w_wa)
e_wa = list([0])
for i in range(len(e)):
    e_wa.append(e_wa[i] + e[i])
#print("e_wa",e_wa)
ans = 1145141919810

for leader in range(N):
    lc = w_wa[leader]
    rc = e_wa[N] - e_wa[leader + 1]
    #print("lc:",lc)
    #print("rc:",rc)
    counter = lc + rc
    #counter = l.count('W') + r.count('E')
    ans = min(counter,ans)

print(ans)

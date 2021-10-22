import copy
str = input()
str = list(str)
N = len(str)
ans = 0
for i in range(2**(N-1)):
    count = 1
    str1 = copy.copy(str)
    for j in range(N-1):
        if ((i >> j) & 1):
            str1.insert(j + count,'+')
            count += 1

    ans += eval("".join(str1))
print(ans)

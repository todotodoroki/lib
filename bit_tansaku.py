str = input()
symbol = ['+','+','+']
n=3
for i in range(2**n):
    for j in range(n):
        if ((i >> j) & 1):
            symbol[j] = '+'
        else:
            symbol[j] = '-'
    y = eval(str[0] + symbol[0] + str[1] + symbol[1] + str[2] + symbol[2] + str[3])
    if y == 7:
        print((str[0] + symbol[0] + str[1] + symbol[1] + str[2] + symbol[2] + str[3])+"=7")
        exit()

S = input()

def con5(str):
    if S[-1] == str[4] and S[-2] == str[3] and  S[-3] == str[2] and S[-4] == str[1] and S[-5] == str[0]:
        return 1
    else:
        return 0

def con6(str):
    if S[-1] == str[5] and S[-2] == str[4] and  S[-3] == str[3] and S[-4] == str[2] and S[-5] == str[1] and S[-5] == str[0]:
        return 1
    else:
        return 0

def con7(str):
    if S[-1] == str[6] and S[-2] == str[5] and  S[-3] == str[4] and S[-4] == str[3] and S[-5] == str[2] and S[-5] == str[1] and S[-6] == str[0]:
        return 1
    else:
        return 0
f1=0
f2=0
f3=0
f4=0
while(1):
    if f1 == 1 and f2 == 1 and f3 == 1 and f4 == 1:
        print("No")
        exit()
    if len(S) == 0:
        print("Yes")
        exit()
    if len(S) >= 5:
        if con5("dream") == 0:
            f1 = 1
        else:
            f1 = 0
            S = S[:-5]

        if con5("erase") == 0:
            f2 = 1
        else:
            f2 = 0
            S = S[:-5]
    else:
        f1 = 1
        f2 = 1

    if len(S) >= 6:
        if con6("eraser") == 0:
            f3 = 1
        else:
            f3 = 0
            S = S[:-6]
    else:
        f3 = 1

    if len(S) >= 7:
        if con7("dreamer") == 0:
            f4 = 1
        else:
            f4 = 0
            S = S[:-7]
    else:
        f4 = 1

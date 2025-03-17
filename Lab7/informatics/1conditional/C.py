val = input()
out = int(input())

res = 1
if(len(val) != 4):
    res = -1
else:
    if(val[0] == val[3] and val[1] == val[2]):
        res = 1
    else:
        res = -1

if(res == 1 and out == 1):
    print('YES')
elif((res == 1 and out != 1) or (res != 1 and out == 1)):
    print('NO')
elif(res != 1 and out != 1):
    print('YES')



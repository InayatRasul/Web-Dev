n = int(input())
arr = list(map(int, input().split()))

i = 1
flag = False
while(i < n):
    if(arr[i - 1] >= 0 and arr[i] >= 0):
        flag = True
        break
    elif(arr[i - 1] < 0 and arr[i] < 0):
        flag = True
        break
    i+=1

if(flag):
    print('YES')
else:
    print('NO')
    
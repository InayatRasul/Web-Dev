n = int(input())
s = input()
arr = s.split()
i = 0
while(i < n):
    if(i % 2 == 0):
        print(arr[i], end=' ')
    i+=1
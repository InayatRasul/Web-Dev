n = int(input())
arr = list(map(int, input().split()))

i = n - 1
while(i >= 0):
    print(arr[i], end=' ')
    i-=1
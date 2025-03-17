n = int(input())
arr = list(map(int, input().split()))

i = 1
res = 0
while(i < n):
    if(arr[i] > arr[i - 1]):
        res+=1
    i+=1
print(res)


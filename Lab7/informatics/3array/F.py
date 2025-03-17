n = int(input())
arr = list(map(int, input().split()))

i = 1
res = 0
while(i < n - 1):
    if( arr[i] > arr[i-1] and arr[i] > arr[i+1]):
        res+=1
    i+=1
print(res)
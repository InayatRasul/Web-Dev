n = int(input())
s = input()
arr = s.split()

i = 0
res = 0
while i < n:
    if(int(arr[i]) > 0):
        res+=1
    i+=1
print(res)
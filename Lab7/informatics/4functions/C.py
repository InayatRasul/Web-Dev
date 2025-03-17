def xor(a,b):
    if(a == b):
        return 0
    return 1
num = list(map(int, input().split()))
print(xor(num[0], num[1]))
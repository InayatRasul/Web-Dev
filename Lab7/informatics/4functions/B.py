def power(a,n):
    return a ** n
num = list(map(float, input().split()))

print(power(num[0], num[1]))
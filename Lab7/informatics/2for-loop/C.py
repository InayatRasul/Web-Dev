a = int(input())
b = int(input())

for i in range(a, b + 1):
    sr = i ** 0.5
    if(sr ** 2 == i):
        print(i, end=' ')

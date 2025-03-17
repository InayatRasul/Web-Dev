x = int(input())
if(x % 180 == 0):
    print(0)
elif(x % 360 < 180):
    print(1)
else:
    print(-1)

# print(-179 % 360)
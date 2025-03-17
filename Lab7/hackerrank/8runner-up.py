if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    ma = -10000
    for i in arr:
        if(i > ma):
            ma = i
    ma2 = -10000
    for i in arr:
        if(i != ma and i > ma2):
            ma2 = i
    print(ma2)
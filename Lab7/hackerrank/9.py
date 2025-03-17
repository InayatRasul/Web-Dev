if __name__ == '__main__':
    n = int(input())
    nl = []
    min = 1000
    smin = 1000
    res = []
    for i in range(n):
        nl.append([])
        name = input()
        score = float(input())
        if(score < min):
            min = score
        nl[i].append(name)
        nl[i].append(score)
    for i in range(n):
        if(nl[i][1] < smin and nl[i][1] != min):
            smin = nl[i][1]
    for i in range(n):
        if(nl[i][1] == smin):
            res.append(nl[i][0])
    res = sorted(res)
    for i in res:
        print(i)
    
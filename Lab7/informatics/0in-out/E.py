v = int(input())
t = int(input())

d = (v * t) % 109
if(d >= 0):
    print(d)
else:
    print(109 + d)

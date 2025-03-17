val = input()
rev_val = ''

for i in reversed(val):
    rev_val = rev_val + i

flag = True
for i in rev_val:
    if(i == '0' and flag == True):
        continue
    else:
        print(i, end='')
        flag = False

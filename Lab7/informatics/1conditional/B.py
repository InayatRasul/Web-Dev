year = int(input())

# res = 'NO' if year % 100 == 0 and year % 400 != 0 else year % 4 == 0 'YES'

if( year % 100 == 0 and year % 400 != 0 ):
    print('NO')
elif(year % 4 == 0):
    print('YES')

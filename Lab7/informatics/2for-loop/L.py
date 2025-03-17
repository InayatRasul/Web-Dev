val = input()
val_len = len(val) - 1

res = 0
for i in range(len(val)):
    res += int(val[i]) * 2**val_len
    val_len-=1
print(res)
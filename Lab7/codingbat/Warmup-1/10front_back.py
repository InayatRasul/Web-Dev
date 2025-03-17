def front_back(str):
  li = list(str)
  str2 = ''
  if(len(str) > 1):
    str2 += li[len(str) - 1]
    for i in range(1,len(str) - 1):
      str2 += li[i]
    str2 += li[0]
  elif(len(str) == 1):
    str2 = li[0]
  return str2

def front_back(str):
  if len(str) <= 1:
    return str
  
  mid = str[1:len(str)-1]  # can be written as str[1:-1]
  
  # last + mid + first
  return str[len(str)-1] + mid + str[0]
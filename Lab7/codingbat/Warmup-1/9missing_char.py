def missing_char(str, n):
  str2 = ''
  it = 0
  for i in str:
    if(it == n):
      it+=1
      continue
    str2 += i
    it+=1
  return str2

# def missing_char(str, n):
#   front = str[:n]   # up to but not including n
#   back = str[n+1:]  # n+1 through end of string
#   return front + back
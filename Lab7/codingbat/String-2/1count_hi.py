def count_hi(str):
  res = 0
  for i in range(0,len(str) - 1):
    if(str[i] == 'h' and str[i+1] =='i'):
      res+=1
  return res

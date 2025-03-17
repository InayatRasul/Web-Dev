def last2(str):
  sub = ''
  res= 0 
  if(len(str) > 1):
    sub = str[len(str)-2 : len(str)]
    for i in range(0, len(str) - 2):
      if(str[i:i+2] == sub):
        res+=1
  return res
      

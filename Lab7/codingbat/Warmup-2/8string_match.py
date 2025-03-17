def string_match(a, b):
  res = 0
  if( len(a) >= 2 and len(b) >= 2):
    for i in range(0,len(a) - 1):
      for j in range(0, len(b) - 1):
        if((i == j) and (a[i: i+2] == b[j: j+2])):
          res+=1
  return res
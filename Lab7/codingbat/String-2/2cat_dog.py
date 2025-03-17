def cat_dog(str):
  cat = 0
  for i in range(0,len(str) - 2):
    if(str[i] == 'c' and str[i+1] =='a' and str[i+2] =='t'):
      cat+=1
  dog = 0
  for i in range(0,len(str) - 2):
    if(str[i] == 'd' and str[i+1] =='o' and str[i+2] =='g'):
      dog+=1
  return cat == dog


def xyz_there(str):
  for i in range(0,len(str) - 2):
    if(i > 0):
      if(str[i-1] != '.' and str[i] == 'x' and str[i+1] =='y' and str[i+2] =='z'):
        return True
    else:
      if(str[i] == 'x' and str[i+1] =='y' and str[i+2] =='z'):
        return True
  return False

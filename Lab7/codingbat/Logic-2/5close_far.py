def is_close(a, num):
  if(abs(a - num) <= 1):
    return True
  return False
def is_far(tar, v1,v2):
  if(abs(tar - v1) >= 2 and abs(tar - v2) >= 2):
    return True
  return False
def close_far(a, b, c):
  if(is_close(a,b) ):
    if(is_far(c,b,a) ):
      return True
  elif(is_close(a,c) ):
    if(is_far(b,c,a) ):
      return True
  return False

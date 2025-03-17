def fix_teen(n):
  if(n >=13 and n <= 19 and n != 15 and n != 16):
    return True
  return False
def no_teen_sum(a, b, c):
  sum = 0
  nums = [a,b,c]
  for i in nums:
    if(not fix_teen(i) ):
      sum+=i
  return sum
  

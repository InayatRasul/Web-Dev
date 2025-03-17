def round10(num):
  if(num % 10 < 5):
    num -= num % 10
  else:
    num += 10- num% 10
  return num
def round_sum(a, b, c):
  sum = 0
  nums = [a,b,c]
  for i in nums:
    sum+=round10(i)
  return sum
    
  

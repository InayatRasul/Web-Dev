def lucky_sum(a, b, c):
  nums = [a,b,c]
  sum = 0
  for i in nums:
    if(i != 13):
      sum+= i
    else:
      break
  return sum

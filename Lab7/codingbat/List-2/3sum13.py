def sum13(nums):
  sum = 0
  skip_next = False
  for i in nums:
    if(skip_next):
      skip_next = False
      continue
    if(i != 13):
      sum+=i
    else:
      skip_next = True
  return sum
     

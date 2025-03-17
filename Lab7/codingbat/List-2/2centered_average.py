def centered_average(nums):
  mi = 1000
  ma = -1000
  sum = 0
  for i in nums:
    sum+=i
    if(i > ma):
      ma = i
  for i in nums:
    if(i < mi):
      mi = i
  return (sum - mi - ma) / (len(nums) - 2)
  

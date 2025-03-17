def big_diff(nums):
  mi = 1000
  ma = -1000
  for i in nums:
    if(i > ma):
      ma = i
  for i in nums:
    if(i < mi):
      mi = i
  return ma - mi

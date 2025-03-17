def sum67(nums):
  sum = 0
  start = False
  for i in nums:
    if(i == 6):
      start = True
    if (i == 7 and start == True):
      start = False
    elif(not start):
      sum+=i
  return sum

def array_front9(nums):
  it = 0
  for i in nums:
    if(i == 9 and it < 4):
      return True
    it+=1
  return False

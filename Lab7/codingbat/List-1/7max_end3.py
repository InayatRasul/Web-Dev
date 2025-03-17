def max_end3(nums):
  if(nums[0] > nums[len(nums) - 1]):
    for i in range(1, len(nums) ):
      nums[i] = nums[0]
  else:
      for i in range(0, len(nums)-1 ):
        nums[i] = nums[len(nums) - 1]
  return nums
    

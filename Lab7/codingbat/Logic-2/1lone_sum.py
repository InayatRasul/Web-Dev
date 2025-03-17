def lone_sum(a, b, c):
  nums = [a,b,c]
  unique=[]
  flag = True
  for i in range(0,3):
    flag = True
    for j in range(0,3):
      if(nums[i] == nums[j] and i != j):
        flag = False
    if(flag):
      unique.append(nums[i])
  sum = 0
  for i in unique:
    sum+=i
  return sum

def make_chocolate(small, big, goal):
  nes5 = goal // 5
  if(nes5 <= big and small >= (goal - nes5 * 5) ):
    return  goal - nes5 * 5
  elif(nes5 > big and small >= (goal - big * 5) ):
    return goal - big * 5
  return -1

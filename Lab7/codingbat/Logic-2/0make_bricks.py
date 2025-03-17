def make_bricks(small, big, goal):
  nec5 = goal // 5
  nec1 = goal - (5 * nec5)
  
  if(nec5 <= big and nec1 <= small):
    return True
  elif(nec5 > big and (goal - big*5) <= small):
    return True

  return False

def string_bits(str):
  str2 = ''
  it = 0
  for i in str:
    if(it % 2 == 0):
      str2 += str[it]
    it+=1
  return str2

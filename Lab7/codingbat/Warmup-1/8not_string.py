def not_string(str):
  if(len(str) >= 3):
    if(str[0] == 'n' and str[1] == 'o' and str[2] == 't'):
      return str
  return 'not ' + str
  
# def not_string(str):
#   if len(str) >= 3 and str[:3] == "not":
#     return str
#   return "not " + str
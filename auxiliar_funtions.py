def temp_plus(temp, degree='2'):
  min_add_temp = 100
  if degree == 2:    
    return temp + min_add_temp
  else:
    return (temp*9/5)+32+(5/9) + min_add_temp
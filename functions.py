def caught_speeding(speed, is_birthday):
  if is_birthday == True:
    speed = speed - 5
  if speed <= 60:
    return 0
  elif speed > 60 and < 81:
    return 1
  elif speed > 81:
    return 2



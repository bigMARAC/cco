while True:
  try:
    monthsList = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 25]
    month, day = map(int, input().split(' '))
    if day == 25 and month == 12:
      print("E natal!")
    elif day == 24 and month == 12:
      print("E vespera de natal!")
    elif day >= 25 and month == 12:
      print("Ja passou!")
    else:
      days = 0
      for i in range(month - 1, len(monthsList)):
        days += monthsList[i]
      days -= day
      print(days)
  except:
      break
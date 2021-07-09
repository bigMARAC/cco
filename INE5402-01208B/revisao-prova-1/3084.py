while True:
  try:
    hour, minute = map(int, input().split(' '))
    hour = hour / 30
    minute = minute / 6
    print("%02d:%02d" % (hour, minute))
  except:
    break
time = int(input())
hours = time // 3600
time = time - (hours * 3600)
minutes = time // 60
time = time - (minutes * 60)

print("%d:%d:%d" % (hours, minutes, time))
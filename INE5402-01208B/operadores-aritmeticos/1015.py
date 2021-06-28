import math
first = list(map(float, input().split(' ')))
second = list(map(float, input().split(' ')))

x = ((second[0] - first[0]) ** 2) + ((second[1] - first[1]) ** 2)
x = math.sqrt(x)
print("%.4f" % x)
length, minimum = map(int, input().split(' '))
data = list(map(int, input().split(' ')))

count = 0
for item in data:
  if item <= 0:
    count += 1

if count >= minimum:
  print("YES")
else:
  print("NO")
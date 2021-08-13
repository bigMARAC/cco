x = int(input()) 
values = list(map(int, input().split(' ')))
values = sorted(values)

for y in range(0, len(values)):
  if values[y] != (y + 1):
    break

if values[y] == (y + 1):
  y += 1

print(y + 1)
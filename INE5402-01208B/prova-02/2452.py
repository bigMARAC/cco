length, x = map(int, input().split(' '))
positions = list(map(int, input().split(' ')))

aux = []
for index in range(len(positions)):
  if index != x - 1:
    aux.append((positions[index + 1] - positions[index]) // 2)

aux.append(positions[0] - 1)
aux.append(length - positions[-1])
print(max(aux))

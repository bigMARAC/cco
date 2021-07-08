count = 0
while True:
  index = int(input())
  if index == 0: break
  aldo, beto = 0, 0
  count += 1

  for i in range(index):
    x, y = map(int, input().split(' '))
    beto += y
    aldo += x

  print("Teste %d" % count)
  if beto > aldo:
    print("Beto\n")
  else:
    print("Aldo\n")
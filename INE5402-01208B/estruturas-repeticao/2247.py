count = 1
while True:
  index = int(input())
  if index == 0: break

  pedrinho, joaozinho = 0, 0
  print("Teste %d" % count)
  count += 1

  for i in range(1, index + 1):
    x, y = map(int, input().split(' '))
    pedrinho += x
    joaozinho += y
    print(pedrinho - joaozinho)
  
  print("")
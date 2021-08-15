index = int(input())
count = 1
for x in range(0, index):
  equals = [0] * 13
  cards = [int(x) for x in input().split()]
  repeat = True

  for index in range(0, len(cards)):
    if sorted(cards) == list(range(min(cards), max(cards) + 1)):
      print("Teste %d\n%d\n" % (count, 200 + min(cards)))
      break

    if cards.count(cards[index]) == 4:
      print("Teste %d\n%d\n" % (count, 180 + cards[index]))
      break

    if len(set(cards)) == len(cards):
      repeat = False

    if cards.count(cards[index]) == 2 and equals[cards[index] - 1] == 0:
      equals[cards[index] - 1] = 2
    if cards.count(cards[index]) == 3 and equals[cards[index] - 1] == 0:
      equals[cards[index] - 1] = 3

  if equals.count(2) == 2:
    final = []
    for y in range(0, len(equals)):
      if equals[y] == 2:
        final.append(y)
    x, y = final[0] + 1, final[1] + 1
    if x + 1 > y + 1:
      value = (3 * x + 2 * y) + 20
    else:
      value = (3 * y + 2 * x) + 20
  elif equals.count(2) == 1 and equals.count(3) == 1:
    value = equals.index(3) + 1 + 160
  elif equals.count(2) == 0 and equals.count(3) == 1:
    value = equals.index(3) + 1 + 140
  elif equals.count(2) == 1 and equals.count(3) == 0:
    value = equals.index(2) + 1
  elif not repeat:
    value = 0
  print("Teste %d\n%d\n" % (count, value))

  count += 1

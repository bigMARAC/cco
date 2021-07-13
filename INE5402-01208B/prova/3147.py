humanos, elfos, anoes, orcs, wargs, aguias = map(int, input().split(' '))

bem = humanos + elfos + anoes
mal = orcs + wargs

if (bem + aguias + 1) > mal:
  print("Middle-earth is safe.")
else:
  print("Sauron has returned.")

'''
  A ideia aqui é bem simples: somar todas as possibilidades para que o lado
  do bem venca: O número do exercito do bem + o número de aguias + o bravo Bilbo
  precisa ser maior que o número de soldados do exercito do mal.
'''
index = int(input())
count = 1
for x in range(0, index):
  # Uma lista auxiliar que começa como
  # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

  equals = [0] * 13
  cards = [int(x) for x in input().split()]
  
  # Uma variável auxiliar para saber se todas as cartas são repetidas
  repeat = True

  for index in range(0, len(cards)):
    # Se as cinco cartas estão em seqüência a partir da carta x
    # a pontuação é x+200 pontos
    if sorted(cards) == list(range(min(cards), max(cards) + 1)):
      value = 200 + min(cards)
      break

    # Se há quatro cartas iguais
    # a pontuação é x+180 pontos
    if cards.count(cards[index]) == 4:
      value = 180 + cards[index]
      break

    # Checa se há alguma carta repetida,
    # se não, não há pontuação
    if len(set(cards)) == len(cards):
      repeat = False

    # Aqui é checado se a carda do index atual é encontrada duas vezes
    # na lista de cartas, se sim, ela será acrescentada na lista auxilias 'equals'
    # na posição correspondente ao seu numero - 1
    # Ex: 1 3 3 5 2, temos dois números 3. A lista auxiliar ficará assim
    # [0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    # O número de repetições (2) na posicação correspondente ao número 3, menos 1
    # A mesma coisa é feita para 3 repetições
    # se tivessemos o input: 5 5 9 9 9, a lista ficaria assim:
    # [0, 0, 0, 0, 2, 0, 0, 0, 3, 0, 0, 0, 0]
    if cards.count(cards[index]) == 2 and equals[cards[index] - 1] == 0:
      equals[cards[index] - 1] = 2
    if cards.count(cards[index]) == 3 and equals[cards[index] - 1] == 0:
      equals[cards[index] - 1] = 3

  # Agora, podemos fazer a checagem utilizando a lista auxiliar
  if equals.count(2) == 2:
    # Se há duas cartas iguais x, duas outras cartas iguais
    # é 3 × x + 2 × y + 20 pontos, em que x > y
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
    # Se há três cartas iguais x e duas outras cartas iguais y
    # a pontuação é x + 160 pontos
    value = equals.index(3) + 1 + 160
  elif equals.count(2) == 0 and equals.count(3) == 1:
    # Se há três cartas iguais x e duas outras cartas diferentes
    # a pontuação é x + 140 pontos
    value = equals.index(3) + 1 + 140
  elif equals.count(2) == 1 and equals.count(3) == 0:
    # Se há apenas duas cartas iguais x e as outras são todas distintas
    # a pontuação é x pontos
    value = equals.index(2) + 1
  elif not repeat:
    value = 0
  print("Teste %d\n%d\n" % (count, value))

  count += 1

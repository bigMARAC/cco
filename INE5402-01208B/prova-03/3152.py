# Função para auxiliar no calculo da área
# utilizando a regra do agrimensor 
def calcArea(vert):
  first = vert[0][0] * vert[1][1]
  first += vert[1][0] * vert[2][1]
  first += vert[2][0] * vert[3][1]
  first += vert[3][0] * vert[0][1]

  second = - (vert[1][0] * vert[0][1])
  second += - (vert[2][0] * vert[1][1])
  second += - (vert[3][0] * vert[2][1])
  second += - (vert[0][0] * vert[3][1])

  determinante = abs(first + second)
  return determinante / 2

vertA = [0] * 4
vertB = [0] * 4

for x in range (0, 4):
  vertA[x] = list(map(int, input().split()))

for i in range (0, 4):
  vertB[i] = list(map(int, input().split()))


if calcArea(vertA) > calcArea(vertB):
  print('terreno A')
else:
  print('terreno B')
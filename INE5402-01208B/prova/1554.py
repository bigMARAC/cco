import math
index = int(input())

for x in range(index):
  bolas = int(input())
  mainX, mainY = map(int, input().split(' '))
  for i in range(bolas):
    x, y = map(int, input().split(' '))
    distancia = math.sqrt(((x - mainX) ** 2) + ((y - mainY) ** 2))
    if i == 0 or distancia < min:
      min = distancia
      num = i + 1
  
  print(num)

'''
  Para resolver esse problema, além de guardarmos todos os valores informados,
  precisamos calcular a distância entre dois pontos em um plano, e pra isso existe
  uma formula: "Subtrair os valores das abscissas de cada ponto e, em seguida, elevar ao quadrado, e fazer o mesmo deve acontecer com os valores das ordenadas" O resultado
  final é a raiz quadrada dessa operação.
  Depois disso precisamos chegar se o valor de cada caso é menor que o caso
  anterior (se for o primeiro caso, o valor da distancia irá assumir o menor valor).
  Agora sabemos sempre que a distância for a menor, e quando ela for a menor, basta
  guardar o index dela.
'''
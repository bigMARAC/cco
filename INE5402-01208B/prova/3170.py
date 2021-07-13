bolinhas = int(input())
galhos = int(input())
if galhos % 2 != 0:
  galhos -= 1

if bolinhas * 2 >= galhos:
  print("Amelia tem todas bolinhas!")
else:
  bolinhas = (galhos / 2) - bolinhas
  print("Faltam %d bolinha(s)" % bolinhas)


'''
  A ideia é primeiro checar se o número de galhos é ímpar, se for ele é 
  arredondado pra baixo. Depois é checado se Amelia ja possui o número
  necessário de bolinhas, se ela não possuir, sabemos que faltam bolinhas,
  então basta fazer a operação pra saber quantas faltam.
'''
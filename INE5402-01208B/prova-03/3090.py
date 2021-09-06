length, width, soldiers = map(int, input().split())

# Aqui é calculado o coeficiente angular do rio
ang = width / length

army01 = 0
army02 = 0

for _ in range(soldiers):
  x, y, abiliity = map(int, input().split())

  # Se x = 0, o exercicito de cima do rio ganha as habilidade,
  # Se y / x (do soldado) for menor que o coeficiente angular
  # do rio, então o soldado está abaixo do rio, portante o exercito
  # 2 ganha a habilidade, caso contrário, o soldado está acima e o
  # exercito 1 ganha a habilidade
  if x == 0:
    army01 += abiliity
  elif y / x < ang:
    army02 += abiliity
  elif y / x > ang:
    army01 += abiliity
  
print('%d %d' % (army01, army02))
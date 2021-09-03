rows, cols = map(int, input().split())
matriz = []

for x in range(rows):
  matriz.append(list(map(int, input().split())))

zeroCols, zeroLine = [], -1
anyTime, valid = False, False
for x in range(rows):
  aux = True

  for y in range(cols):
    
    # Aqui é checado se a coluna atual precisa ser uma coluna de zeros
    if y in zeroCols:
      # Se precisar, é checado se o número atual e zero e se essa regra
      # já foi quebrada alguma vez
      if matriz[x][y] == 0 and not anyTime:
        valid = True
      else:
        valid = False
        anyTime = True
        break
    
    # Aqui é checado se o número atual é diferente de zero e 
    # se o número a sua esquerda é um zero, se isso for verdadeiro
    # então todos os próximos números dessa coluna precisarão ser zero
    if matriz[x][y] != 0 or y == 0:
      if y == 0 or matriz[x][y - 1] == 0:
        zeroCols.append(y)
    else:
      aux = False

    if zeroLine >= 0 and zeroLine == x - 1:
      if matriz[x][y] != 0:
        valid = False
        break
  
  if aux:
    zeroLine = x

if (valid):
  print('S')
else:
  print('N')
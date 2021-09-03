rows, cols = map(int, input().split())
matriz = []

for x in range(rows):
  matriz.append(list(map(int, input().split())))

valid = True
all_zeros = False
qtd_zeros_ultima_linha = -1

for i in range(rows):
  j = 0
  try:
    while matriz[i][j] == 0:
      j += 1
  except IndexError:
    all_zeros = True

  if not all_zeros:
    if j <= qtd_zeros_ultima_linha:
      valid = False
      break
    else:
      qtd_zeros_ultima_linha = j
  else:
    if j != cols:
      valid = False
      break

if valid:
  print('S')
else:
  print('N')
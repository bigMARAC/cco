index = int(input())

for mainIdx in range(index):
  N, L = map(int, input().split(' '))
  matriz = [0] * (N + 1)

  # Criação de uma matriz auxiliar que ira guardar as posições em que se encontram
  # as somas, na matriz principal, exemplo:
  # se a matriz for = [[0, 0, 0, 0], [0, 3, 101, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
  # então, aux será = [[1, 1], [1, 2]]
  aux = [] 

  for i in range(0, N + 1): # Criação da matriz, conforme o enunciado
    matriz[i] = [0] * (N + 1)
  
  for x in range(0, L):
    P, l, c, v = map(int, input().split(' '))
    if [l, c] not in aux:
      aux.append([l, c]) 
    matriz[l][c] += v
  
  # Os itens da matriz auxiliar serão ordenados,
  # de acordo com o solicitado no enunciado
  aux.sort(key = lambda item: item[0])
  
  for idx, pos in enumerate(aux):
    linha, coluna = pos[0], pos[1]
    print('%d %d %d' % (linha, coluna, matriz[linha][coluna]))
    
  if mainIdx != index - 1:
    print()

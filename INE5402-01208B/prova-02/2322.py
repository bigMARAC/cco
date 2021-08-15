x = int(input()) 
values = list(map(int, input().split(' ')))
values = sorted(values)

# Depois de ordenar a lista, basta fazer um simples IF
# pra saber que peça está faltando
for y in range(0, len(values)):
  if values[y] != (y + 1):
    break

# Se no primeiro loop não foi encontrada a peça que falta
# Então provavelmente a peça que falta é a última peça
# Ex.: 1 2 3, a peça que falta é a 4
if values[y] == (y + 1):
  y += 1

print(y + 1)
# Esse problema é bastante simples, basta checar
# se o valor fornecido já faz parte de matriz,
# se fizer significa que é repetido
length = int(input())
matriz = []
rep, uniq = 0, 0
for _ in range(length):
  value = int(input())

  if value not in matriz:
    matriz.append(value)
    uniq += 1
  else:
    rep += 1
  
print(uniq)
print(rep)
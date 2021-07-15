index = int(input())
verba, gasto = 0, 0

for _ in range(index):
  tipo, valor = input().split(' ')
  if tipo == 'G':
    gasto += int(valor)
  if tipo == 'V':
    verba += int(valor)

if verba >= gasto:
  print("A greve vai parar.")
else:
  print("NAO VAI TER CORTE, VAI TER LUTA!")

'''
  Para resolver esse problema basta guardar os valores de verba e gastos
  separadamente e no final checar se o valor da verba é maior ou igual ao
  valor dos gastos.
'''
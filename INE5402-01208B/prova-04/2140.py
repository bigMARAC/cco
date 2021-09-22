notas = [2, 5, 10, 20, 50, 100]

# Basta checar se subtrairmos o Troco de uma nota X
# podemos obter exatamente o valor de alguma nota
# menor que X
# Exemplo: # Valor = 11 - Pago = 23 - Troco = 12
# 12 - 10 = 2

while True:
  valor, pago = map(int, input().split())
  if pago + valor == 0: break;
  final = pago - valor

  possivel = False

  for x in range(len(notas)):
    if possivel:
      break
    for i in range(len(notas)):
      if final - notas[i] == notas[x]:
        possivel = True
        break

  if possivel:
    print('possible')
  else:
    print('impossible')

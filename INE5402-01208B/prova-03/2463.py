# Para resolver esse problema basta ir incrementando
# uma variável auxiliar e sempre que ela for maior que
# o maior número obtido teremos o novo maior número obtido
length = int(input())
matriz = list(map(int, input().split()))
soma, maior = 0, 0

for x in range(length):
  soma += matriz[x]

  if soma < 0:
    soma = 0
  
  if soma > maior:
    maior = soma

print(maior)

x1, x2 = map(int, input().split(' '))
final = []
for x in range(x1, 1, -1):
  prime = True
  for i in range(2, x + 1):
    if x % i == 0 and x != i:
      prime = False
  if prime:
    final.append(x)
    break

for x in range(x2, 1, -1):
  prime = True
  for i in range(2, x + 1):
    if x % i == 0 and x != i:
      prime = False
  if prime:
    final.append(x)
    break

print(final[0] * final[1])

'''
  Obs.: Para um número ser primo ele só pode dividir ele mesmo e 1.
  Para a resolução desse problema, depois de guardar os valores x1 e x2 fornecidos pelo
  usuário, foi necessário calcular o número primo mais perto de x1 ou x2. para isso
  foi preciso o primeiro 'for' que vai de x1 até 0, e dentro desse temos um outro
  'for' que vai de 2 até X, com isso podemos ver se i é divisor de algum número além
  dele mesmo (todos os números são divisiveis por 1). Se o número for primo a
  variável 'prime' recebe o valor True e o número é adicionado na lista final,
  depois de algum número ser adicionado, o laço de repetição é encerrado, porque
  o primeiro número que foi adicionado é o número mais próximo de x1 ou x2.
  Por fim, basta mostrar o produto desses dois números.
'''
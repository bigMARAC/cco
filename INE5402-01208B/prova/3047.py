monica = int(input())
f1 = int(input())
f2 = int(input())
idades = [f1, f2, (monica - (f1 + f2))]

final = sorted(idades)

print(final[2])

'''
  Esse problema é simples de ser resolvido, basta adicionar as 2 idades dos filhos
  em uma lista e adicionar também o calculo da idade do 3° filho, depois disso
  basta ordernar a lista e mostrar o maior valor, que será a idade do filho mais
  velho.
'''
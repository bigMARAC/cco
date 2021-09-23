length, total = map(int, input().split())
runes = {}
final = 0

# Para resolver esse problema basta guardar
# os valores das runas e seus nomes em um dicionario
# e depois somar o valor das runas recitadas e comparar
# com o valor necessário.

for _ in range(length):
  key, value = input().split()
  runes[key] = int(value)

_ = input()
recited = list(input().split())

for x in recited:
  final += runes[x]

print(final)

if final >= total:
  print('You shall pass!')
else:
  print('My precioooous')

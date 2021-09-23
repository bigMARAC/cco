length = int(input())

for x in range(length):
  filtros = list(map(int, input().split()))
  print((sum(filtros) + 1) - (filtros[0] * 2))

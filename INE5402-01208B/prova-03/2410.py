index = int(input())
aux = []

for _ in range(index):
  aux.append(int(input()))

# Aqui é usado o auxilio da coleção, que só permite valores
# únicos, logo os valores repetidos serão excluidos
final = len(list(set(aux)))

print(final)
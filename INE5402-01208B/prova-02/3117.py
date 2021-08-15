length, minimum = map(int, input().split(' '))
data = list(map(int, input().split(' ')))

count = 0

# Aqui, fazemos um loop em todos os tempos
# da lista 'data', se algum desses tempos for
# menor ou igual a 0, significa que esse aluno
# não se atrasou, então incrementamos a variável
# auxiliar. No final, checamos se a quantidade de
# alunos que não se atrasaram, é maior ou igual
# a quantidade de alunos minima informada pelo professor
for item in data:
  if item <= 0:
    count += 1

if count >= minimum:
  print("YES")
else:
  print("NO")
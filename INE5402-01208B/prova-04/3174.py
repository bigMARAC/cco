length = int(input())

# Essa questão foi resolvida com a ajuda de dois dicionários,
# um pra guardar a quantidade de horas que cada grupo precisa
# pra fazer um presente e outro pra guardar a quantidade de horas
# que cada grupo irá trabalhar. Depois disso basta fazer uma divisão
# inteira para obter o resultado

grupos = {'bonecos': 0, 'arquitetos': 0, 'musicos': 0, 'desenhistas': 0}
horas = {'bonecos': 8, 'arquitetos': 4, 'musicos': 6, 'desenhistas': 12}

for x in range(length):
  _, tipo, hora = input().split()
  hora = int(hora)
  grupos[tipo] += hora

count = 0
for key in grupos.keys():
  count += grupos[key] // horas[key]

print(count)

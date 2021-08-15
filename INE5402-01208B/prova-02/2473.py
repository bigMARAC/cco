values = list(map(int, input().split(' ')))
winning = list(map(int, input().split(' ')))
count = 0

# Esse problema é bastante simples, basta fazer um loop
# nos números apostados e dentro desse, fazer um loop nos
# números certos, depois é só comporar o número X com os N
# números certos, e incrementar o 'count' toda vez que algum
# número for igual
for item in values:
  for number in winning:
    if item == number:
      count += 1

if count == 3:
  print("terno")
elif count == 4:
  print("quadra")
elif count == 5:
  print("quina")
elif count == 6:
  print("sena")
else:
  print("azar")
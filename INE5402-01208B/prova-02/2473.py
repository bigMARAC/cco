values = list(map(int, input().split(' ')))
winning = list(map(int, input().split(' ')))
count = 0

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
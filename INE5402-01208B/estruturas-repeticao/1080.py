final = [0]
for x in range(1, 5):
  number = int(input())
  final.append(number)

value = max(final)
print(value)
print(final.index(value))
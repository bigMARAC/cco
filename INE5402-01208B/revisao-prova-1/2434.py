index, total = map(int, input().split(' '))
final = []

for _ in range(index):
  value = int(input())
  total += value
  final.append(total)

print(sorted(final)[0])
import re
length = int(input())

# Para resolver esse problema bastou o uso
# de expressões regulares para encontrar todas
# as ocorrências exatas da palavra informada

for _ in range(length):
  positions = []
  string = input()
  word = r'\b%s\b' % input()
  word = re.compile(word)
  final_string = ""

  for match in re.finditer(word, string):
    positions.append(match.start())

  if len(positions) == 0: 
    print('-1')
  else:
    for pos in positions:
      final_string += " " + str(pos)
    print(final_string.strip())

length = int(input())
chars = ['Q', 'J', 'K', 'A']

# Para resolver esse problema basta percorrer
# todos oso caracteres da string informada, procurando
# os 4 caracteres informados pelo enunciado

for x in range(length):
  string = input()
  count = 0
  resp = []

  for char in string:
    if chars.count(char) == 1 and resp.count(char) == 0:
      count += 1
      resp.append(char)
    
    if count == 4:
      break

  if count == 4:
    print('Aaah muleke')
  else: 
    print('Ooo raca viu')

# Para resolver esse problema foi necessário criar
# um dicionário com a representação das teclas e depois
# disso, percorrer todos os caracteres da string informada
# e procurar a sua tecla de equivalência, após só foi
# preciso concatenar o numero da tecla na string final.

buttons = {
  0: ' ',
  2: 'abc',
  3: 'def',
  4: 'ghi',
  5: 'jkl',
  6: 'mno',
  7: 'pqrs',
  8: 'tuv',
  9: 'wxyz',
}

length = int(input())

for x in range(length):
  string = input()
  final_string = ''

  for x in string:
    for button, chars in buttons.items():
      for j in range(len(chars)):
        if x == chars[j]:
          if len(final_string) >= 1 and final_string[len(final_string) - 1] == str(button):
            final_string += "*" + str(button) * (j + 1)
          else:
            final_string += str(button) * (j + 1)
        elif x == chars[j].upper():
          final_string += "#" + str(button) * (j + 1)

  print(final_string)

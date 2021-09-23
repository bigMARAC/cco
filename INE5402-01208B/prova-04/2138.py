while True:
  try:
    num = input()
    bigger = -1
    amount = -1

    # Para resolver esse problema basta fazer uma laço
    # de repetição que percorre os caracteres possíveis
    # e checar qual aparece mais vezes

    for x in range(0, 10):
      if num.count('%d' % x) >= amount and bigger < x:
        bigger = x
        amount = num.count('%d' % x)

    print(bigger)
  except:
    break

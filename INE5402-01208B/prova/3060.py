valor = int(input())
parcela = int(input())

if valor % parcela == 0:
  for _ in range(parcela):
    print(valor // parcela)
else:
  final = []
  resto = valor % parcela
  for _ in range(parcela):
    final.append(valor // parcela)

  for x in range(resto):
    final[x] += 1

  for x in range(len(final)):
    print(final[x])
  
'''
  Para resolver esse problema, primeir resolvemos o caso mais simples que é
  quando o valor total é divisivel pelo número de parcelas, basta mostrar o valor
  de cada parcela. O outro caso é o contrário do primeiro, então o valor do resto
  é salvo em uma variável para ser dividido igualmente entre as parcelas, o valor
  inteiro da divisão é salvo numa lista, onde cada posição corresponde a uma parcela,
  depois disso o valor que sobrou é dividido igualmente nas parcelas.
'''
base = int(input())
final = int(input())

if base == 160 - final:
  print(0)
elif base > 160 - final:
  print(1)
else:
  print(2)

'''
  Para resolver esse problema primeiro é necessário abstrair que o corte se
  encerra em 'final', portanto se 160 (tamanho total do comprimento) menos 
  o final, for menor que o ponto inicial do corte da base, siginifica que o 
  corte terminou no lado esquerdo, portanto Felix venceu. Se forem iguais, 
  significa que o corte foi feito no meio da nota, e o último caso que sobra 
  é Marzia vencer.
'''
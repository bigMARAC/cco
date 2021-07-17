x = int(input())
y = int(input())

if x >= 6 and y >= 6:
  if x >= 18 or y >= 18:
    print("YES")
  elif x>= 14 and y >= 14:
    print("YES")
  else:
    print("NO")
else:
  print("NO")

'''
  Para resolver esse problema foram necessários 'IFs' simples, que fossem de 
  acordo com o enunciado da questão
'''
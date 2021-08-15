index = int(input())
girls, boys = 0, 0

# Nesse problema, pegamos o segundo valor do input
# que informa o sexo da criança e incrementamos
# a váriavel de acordo com o valor recebido
for x in range (0, index):
  gift_type = list(input().split(' '))[1]
  if gift_type == 'M':
    boys += 1
  else:
    girls += 1
  

print("%d carrinhos" % boys)
print("%d bonecas" % girls)
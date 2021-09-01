o = input()

mat = [None] * 12
for i in range(0, 12):
	mat[i] = [None] * 12

for i in range(0,12):
	for j in range(0,12):
		mat[i][j] = float(input())
        
soma = 0;
qtde = (144 - 24) / 4 #Computo a quantidade de valores existentes naquela área superior
for i in range(7,12): #Percorro apenas os elementos que encontram-se na região verde... 
  for j in range(12 - i, i): #Vou da coluna 12-i até a coluna i-1
    soma += mat[i][j]

if o == 'S':
  print("%.1f" % soma)
else:
  print("%.1f" % (soma / qtde))
	

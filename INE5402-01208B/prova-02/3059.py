length, minimum, maximum = map(int, input().split(' '))
numbers = list(map(int, input().split(' ')))

count = 0

# Basta fazer um loop X nos números e depois um loop Y
# e dentro do loop Y, podemos checar se a soma do número
# do loop X com o número do loop Y está de acordo com
# as regras recebidas por input, se sim, incrementamos a 
# váriavel auxiliar. No final precisamos dividir por dois
# visto que o IF será aceito em duas ocasiões iguais
for num in numbers:
  for num_aux in numbers:
    if num != num_aux and num + num_aux <= maximum and num + num_aux >= minimum:
      count += 1

print(count // 2)
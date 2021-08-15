length, x = map(int, input().split(' '))
positions = list(map(int, input().split(' ')))

aux = []

# Nesse problema foi um pouco mais díficil de encontrar
# um 'padrão', mas depois de analisar as imagens podemos
# chegar a conclusão que, se cada quadradinho representa 1 dia,
# o tempo para completar a fita é a maior distância entre um
# ponto e outro, mas dividida na metade, uma vez que os dois
# pontos avançam um dia
for index in range(len(positions)):
  if index != x - 1:
    aux.append((positions[index + 1] - positions[index]) // 2)

# Adicionamos na lista auxiliar o tempo do primeiro
# quadradinho até a última posição da lista, e do último
# até a primeira posição
aux.append(positions[0] - 1)
aux.append(length - positions[-1])

# Agora basta apresentar o maior valor dentre todos,
# Conforme explicado no primeiro bloco de comentários
print(max(aux))

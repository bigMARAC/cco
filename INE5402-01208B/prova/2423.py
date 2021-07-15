xicara, ovo, leite = map(int, input().split(' '))
receita = []

receita.append(xicara // 2)
receita.append(ovo // 3)
receita.append(leite // 5)

print(min(receita))

'''
  Para fazer esse exercicio basta conseguir o resultado da divisão inteira de 
  cada uma das variáveis pelos seus respectivos valores da receita inicial e
  salvar em uma lista para facilitar. Depois disso só é necessário mostrar o 
  menor valor da lista.
'''
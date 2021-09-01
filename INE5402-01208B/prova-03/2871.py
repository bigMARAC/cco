while True:
  try:
    linhas, _ = map(int, input().split(' '))
    saca, litro, final = 0, 0, 0

    for lin in range(0, linhas):
      # Os valores informados são somados e guardados
      # na variável 'final', e por fim são usados para
      # apresentar a respectiva resposta de acordo com
      # o enunciado
      final += sum([int(i) for i in input().split()])

    if final < 60:
      litro = final
    elif final == 60:
      saca = 1
    else:
      litro = final % 60
      saca = final // 60

    print('%d saca(s) e %d litro(s)' % (saca, litro))
  except:
    break
n1, n2, n3, n4 = map(float, input().split(' '))
media = ((n1 * 2) + (n2 * 3) + (n3 * 4) + (n4 * 1)) / 10

print('Media: {:.1f}'.format(media))

if media >= 7.0:
    print("Aluno aprovado.")
if media < 5.0: 
    print("Aluno reprovado.")
if media >= 5 and media <= 6.9:
    print("Aluno em exame.")
    n5 = float(input())
    print("Nota do exame:", n5)
    final = (n5 + media) / 2
    if final >= 5:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    print("Media final:", final)
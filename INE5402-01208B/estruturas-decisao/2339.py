data = list(map(int, input().split(' ')))
data.sort()
x, y, z = data

if (x + y) <= z:
    print("Invalido")
else:
    if x == y and x == z:
        print("Valido-Equilatero")
    elif x == y or y == z:
        print("Valido-Isoceles")
    else:
        print("Valido-Escaleno")
    print("Retangulo:", "S" if ((x ** 2) + (y ** 2)) == z ** 2 else "N")

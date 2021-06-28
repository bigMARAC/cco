x, y, z = map(float, input().split(' '))

triangulo = (x * z) / 2
circulo = (z ** 2) * 3.14159
trapezio = ((x + y) * z) / 2
quadrado = y ** 2
retangulo = x * y

print("TRIANGULO: %.3f" % triangulo)
print("CIRCULO: %.3f" % circulo)
print("TRAPEZIO: %.3f" % trapezio)
print("QUADRADO: %.3f" % quadrado)
print("RETANGULO: %.3f" % retangulo)
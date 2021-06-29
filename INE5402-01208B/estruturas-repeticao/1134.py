data = [0, 0, 0,0]
while True:
    code = int(input())
    if code == 4:
        break
    if code in (1, 2, 3):
        data[code] += 1
print("MUITO OBRIGADO")
print("Alcool:", data[1])
print("Gasolina:", data[2])
print("Diesel:", data[3])
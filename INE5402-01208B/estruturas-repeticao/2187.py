data = []
while True:
    x = int(input())
    if x == 0:
        break
    data.append(x)

for i, value in enumerate(data):
    print("Teste", i + 1)
    fifity = value // 50
    value = value - (fifity * 50)
    ten = value // 10
    value = value - (ten * 10)
    five = value // 5
    one = value - (five * 5)
    print("%d %d %d %d\n" % (fifity, ten, five, one))
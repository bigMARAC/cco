index = int(input())

for i in range(index):
    data = list(map(int, input().split()))
    matriz = [[data[0], data[1], 1], [data[2], data[3], 1], [data[4], data[5], 1]]
    final = matriz[0][0] * matriz[1][1] * matriz[2][2]
    final += matriz[0][1] * matriz[1][2] * matriz[2][0]
    final += matriz[0][2] * matriz[1][0] * matriz[2][1]

    final -= matriz[0][1] * matriz[1][0] * matriz[2][2]
    final -= matriz[0][0] * matriz[1][2] * matriz[2][1]
    final -= matriz[0][2] * matriz[1][1] * matriz[2][0]
    
    print("%.3f" % ((1/2) * final))
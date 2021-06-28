data = list(map(int, input().split(' ')))
data[0] = data[0] * 3
data[3] = data[3] * 3

if (data[0] + data[1]) == (data[3] + data[4]):
    if data[2] == data[5]:
        print("=")
    elif data[2] > data[5]:
        print("C")
    else:
        print("F")
elif (data[0] + data[1]) > (data[3] + data[4]):
    print("C")
else:
    print("F")
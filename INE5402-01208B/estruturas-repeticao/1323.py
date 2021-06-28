infos = [0]
for x in range(1, 101):
    infos.append((x ** 2) + infos[x - 1])

while(True):
    num = int(input())
    
    if num == 0:
        break
    
    print(infos[num])
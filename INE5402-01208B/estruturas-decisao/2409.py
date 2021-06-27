bed = list(map(int, input().split(' ')))
door = list(map(int, input().split(' ')))
bed.sort()
door.sort()

if door[0] >= bed[0] and bed[1] <= door[1]:
    print("S")
else:
    print("N")
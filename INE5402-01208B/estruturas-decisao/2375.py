diameter = int(input())
height, width, depth = map(int, input().split(' '))

if diameter <= height and diameter <= width and diameter <= depth:
    print("S")
else:
    print("N")
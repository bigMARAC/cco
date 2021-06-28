import math 
width, height , profundidade, depth = map(int, input().split(' '))
depth = depth * 2
square = math.sqrt(((width*width) + (height  * height ) + (profundidade * profundidade)))

if depth >= square:
    print("S")
else:
    print("N")
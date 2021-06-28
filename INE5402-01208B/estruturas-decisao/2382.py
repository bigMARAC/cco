import math 
width, height , depth, radius = map(int, input().split(' '))
diameter = radius * 2
square = math.sqrt(((width*width) + (height  * height ) + (depth * depth)))

if diameter >= square:
    print("S")
else:
    print("N")
count = 0
while True:
    count += 1
    x = int(input())
    if x == -1: break

    parts = ((1 + (2 ** x)) * (1 + (2 ** x)))
    
    print("Teste %d" % count)
    print("%d\n" % parts)

x = int(input())

for _ in range(0, x):
    number = int(input())
    if number == 0:
        print("NULL")
    elif number % 2 == 0:
        print("EVEN %s" % ("POSITIVE" if number > 0 else "NEGATIVE"))
    else:
        print("ODD %s" % ("POSITIVE" if number > 0 else "NEGATIVE"))
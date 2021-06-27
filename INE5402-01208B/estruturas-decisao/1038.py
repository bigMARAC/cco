index, count = map(int, input().split(' '))

items = [4.00, 4.50, 5.00, 2.00, 1.50]

print("Total: R$ %.2f" % (items[index - 1] * count))
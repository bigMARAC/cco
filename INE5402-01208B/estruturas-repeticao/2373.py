count = int(input())
final = 0

for i in range(0, count):
    l, c = map(int, input().split(' '))
    if l > c:
        final += c

print(final)
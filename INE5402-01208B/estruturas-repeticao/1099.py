count = int(input())

for _ in range(0, count):
    final = 0
    numbers = list(map(int, input().split(' ')))
    numbers.sort()

    for i in range(numbers[0] + 1, numbers[1]):
        if i % 2 != 0:
            final += i

    print(final)
first = list(map(int, input().split(' ')))
second = list(map(int, input().split(' ')))

if (first[1] / first[2]) <= (second[1] / second[2]):
    print(first[0])
else:
    print(second[0])
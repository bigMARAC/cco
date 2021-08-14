length, minimum, maximum = map(int, input().split(' '))
numbers = list(map(int, input().split(' ')))

count = 0
for num in numbers:
  for num_aux in numbers:
    if num != num_aux and num + num_aux <= maximum and num + num_aux >= minimum:
      count += 1

print(count // 2)
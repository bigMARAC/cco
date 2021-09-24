# Para resolver esse problema, basta calcular o
# MMC dos 3 números e subtrair o primeiro valor
# informado


# returns the first prime number after index
def get_next_prime_number(index: int) -> int:
  if index >= 997:
    return 997

  for x in range(index + 1, 1000):
    prime = True
    for y in range(1, 1000):
      if y != 1 and x % y == 0 and x != y:
        prime = False
    if prime:
      if x == 1:
        return 2
      return x

def calc_mmc(numbers: list) -> int:
  aux = []
  while True:
    breaker = False
    for x in range(0, numbers[2]):
      if breaker: break
      prime_number = get_next_prime_number(x)
      for idx in range(len(numbers)):
        if numbers[idx] %  prime_number == 0:
          aux.append(prime_number)
          print('num: %d - prime: %d' % (numbers[idx], prime_number))
          print(numbers)
          numbers[idx] = numbers[idx] // prime_number
          breaker = True
          break

    if sum(numbers) == 3:
      break
  print(aux)
# while True:
#   try:
last = int(input())
numbers = list(map(int, input().split()))
calc_mmc(numbers)
# print(calc_mmc(numbers) - last)
#   except:
#     break
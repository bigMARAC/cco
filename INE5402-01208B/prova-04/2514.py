# Para resolver esse problema, basta calcular o
# MMC dos 3 números e subtrair o primeiro valor
# informado


# retorna o mdc de dois números
def calc_mdc(n1: int, n2: int) -> int:
  while(n1):
    n2, n1 = n1, n2 % n1
  return n2

# retorna o mmc de 3 números
def calc_mmc(n1: int, n2: int, n3: int) -> int:
  mdc = calc_mdc(n1, n2)

  mmc = (n1 * n2) // mdc
  return (n3 * mmc) // calc_mdc(n3, mmc)

while True:
  try:
    last = int(input())
    n1, n2, n3 = map(int, input().split())
    print(calc_mmc(n1, n2, n3) - last)
  except:
    break

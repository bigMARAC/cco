index = int(input())
pattern = [1, 2, 3, 4, 5, 6]

for i in range(1, index + 1):
  top = int(input())
  middle = list(map(int, input().split(' ')))
  down = int(input())
  
  dummy = middle
  dummy.append(top)
  dummy.append(down)

  final = sorted(dummy)

  if final == pattern and top + down == 7 and middle[0] + middle[2] == 7 and middle[1] + middle[3] == 7:
    print("SIM")
  else:
    print("NAO")
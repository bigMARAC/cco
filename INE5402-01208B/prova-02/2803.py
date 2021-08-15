statesList = ["acre", "amapa", "amazonas", "para", "rondonia", "roraima", "tocantins"]
state = input()

# Pra esse problema basta ter uma lista com todos 
# os estados da região norte e checar e o valor
# recebido no input está nessa lista
if state in statesList:
  print("Regiao Norte")
else:
  print("Outra regiao")
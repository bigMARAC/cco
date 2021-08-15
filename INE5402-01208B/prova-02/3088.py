# Um problema bastante simples,
# basta substituir o conjunto de caracteres
# ' ,' e ' .' pelos caracteres ',' e '.'
while True:
  try:
    text = input()
    if text == "": break;
    text = text.replace(" ,", ",")
    text = text.replace(" .", ".")
    print(text)
  except:
    break
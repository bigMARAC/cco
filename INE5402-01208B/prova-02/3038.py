while True:
  try:
    text = input()
    if text == "": break;

    # Basta usar a função replace no texto
    # substituindo todos os caracteres oferecidos
    # pelo problema
    text = text.replace("@", "a")
    text = text.replace("&", "e")
    text = text.replace("!", "i")
    text = text.replace("*", "o")
    text = text.replace("#", "u")
    print(text)
  except:
    break
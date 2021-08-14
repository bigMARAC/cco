while True:
  try:
    text = input()
    if text == "": break;
    text = text.replace("@", "a")
    text = text.replace("&", "e")
    text = text.replace("!", "i")
    text = text.replace("*", "o")
    text = text.replace("#", "u")
    print(text)
  except:
    break
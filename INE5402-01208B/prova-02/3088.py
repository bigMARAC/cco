while True:
  try:
    text = input()
    if text == "": break;
    text = text.replace(" ,", ",")
    text = text.replace(" .", ".")
    print(text)
  except:
    break
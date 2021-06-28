dias = int(input())

ano = dias // 365
dias = dias - ano * 365

mes = dias // 30
dias = dias - mes * 30

print("%.0f ano(s)" % ano)
print("%.0f mes(es)" % mes)
print("%.0f dia(s)" % dias)
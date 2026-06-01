# Validando se é ano bissexto

from datetime import date

ano_escolhido = int(input("Digite o ano que vc quer saber se é bissexto (0 para o ano atual): "))
if ano_escolhido == 0:
    ano_escolhido = date.today()
if ano_escolhido % 4 == 0 and ano_escolhido % 100 != 0 or ano_escolhido % 400 == 0:
    print(f"{ano_escolhido} é ano bissexto!")
else:
    print(f"{ano_escolhido} não é bissexto")
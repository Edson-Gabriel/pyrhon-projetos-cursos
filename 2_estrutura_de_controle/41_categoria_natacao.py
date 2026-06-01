# Faça um programa para informar qual categoria o usuário se encaixa
# com base na idade

from datetime import date
data_nascimento = int(input("Informe seu ano de nascimento: "))
idade = date.today().year - data_nascimento
print(f"Você tem {idade} anos")
if idade <= 9:
    print("Categoria MIRIM")
elif idade <= 14:
    print("Categoria INFANTIL")
elif idade <= 19:
    print("Categoria JUNIOR")
elif idade <= 20:
    print("Categoria SÊNIOR")
elif idade > 20:
    print("Categoria MASTER")
print("Boa sorte na sua categoria!")
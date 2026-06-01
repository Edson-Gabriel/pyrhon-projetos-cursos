# Verificando quantas pessoas são maiores de idades.

from datetime import date
maioridade = 0
menor_idade = 0
for i in range(7):
    ano_nascimento = int(input("Informe seu ano de nascimento: "))
    if date.today().year - ano_nascimento >= 21:
        maioridade += 1
    else:
        menor_idade += 1

print(f"{maioridade} pessoas são maiores de idades")
print(f"{menor_idade} pessoas são menores de idades")
# Verificando se ainda vou me alistar, se já tenho que me alistar ou 
# se já passou o período de alistamento.

from datetime import date
sexo = input("Informe seu gênero [F para Feminino e M para Masculino]: ").upper().strip()
if sexo == "M":
    ano_nascimento = int(input("Digite o ano do seu nascimento: "))
    ano_atual = date.today().year
    idade = ano_atual - ano_nascimento
    if idade < 18:
        print("Menor de idade! (Proibido alistamento)")
        print(f"Ainda faltam {18 - idade} ano(s) para você se alistar.")
    elif idade == 18:
        print(f"{idade} anos?! Parabéns, hora do alistamento obrigatório.")
    elif idade > 18:
        print(f"Você tem {idade} anos! Passou {idade - 18} ano(s) do perído de alistamento.")
    else:
        print("Valor incorreto.")
elif sexo == "F":
    print("Alistamento não obrigatório!")
else:
    print("Dados inválidos (F para Feminino e M para Masculino)")
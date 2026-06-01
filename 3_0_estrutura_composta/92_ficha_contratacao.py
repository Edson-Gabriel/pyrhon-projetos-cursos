# Crie um programa que leia nome, ano de nascimento e carteira 
# de trabalho e cadastre-o (com idade) em um dicionário. Se 
# por acaso a CTPS for diferente de ZERO, o dicionário receberá 
# também o ano de contratação e o salário. Calcule e acrescente, 
# além da idade, com quantos anos a pessoa vai se aposentar.

from datetime import datetime
ficha_funcionario = {
}
ficha_funcionario['nome'] = input("Nome: ")
data_nascimento = int(input("Ano de nascimento: "))
ficha_funcionario['idade'] = datetime.now().year - data_nascimento
ficha_funcionario['carteira_trabalho'] = int(input("Carteira de trabalho (0 se não tiver): "))
if ficha_funcionario['carteira_trabalho'] != 0:
    ficha_funcionario['contratacao'] = int(input("Ano de contratação: " ))
    ficha_funcionario['salario'] = float(input("salário: R$" ))
    ficha_funcionario['aposentadoria'] = ficha_funcionario['idade'] + ((ficha_funcionario['contratacao'] + 35) - datetime.now().year)
for key, valor in ficha_funcionario.items():
    print(f"{key} tem o valor {valor}")
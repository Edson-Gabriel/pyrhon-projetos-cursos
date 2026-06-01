# Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
# OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

valor_a_sacar = int(input("Informe o valor a ser sacado: R$"))
cedula = 50 #20, 10 e 1
total_cedula = 0
while True:
    if valor_a_sacar >= cedula:
        valor_a_sacar -= cedula
        total_cedula += 1
    else:
        if total_cedula > 0:
            print(f"Total de {total_cedula} cédulas de R${cedula:.2f}")
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        total_cedula = 0
        if valor_a_sacar == 0:
            break
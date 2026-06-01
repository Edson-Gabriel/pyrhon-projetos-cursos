#Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.

while True:
    numero_1 = int(input("Informe o primeiro número: "))
    numero_2 = int(input("Informe o segundo número: "))
    print("[1] SOMAR\n[2] MULTIPLICAR\n[3] MAIOR\n[4] NOVOS NÚMEROS\n[5] SAIR")
    opcao = int(input("Escolha uma opção: "))
    if opcao == 1:
        print("Opção escolhida SOMAR")
        print(f"{numero_1:2} + {numero_2:2} = {numero_1 + numero_2}")
    elif opcao == 2:
        print("Opção escolhida MULTIPLICAR")
        print(f"{numero_1:2} X {numero_2:2} = {numero_1 * numero_2}")
    elif opcao ==3:
        if numero_1 > numero_2:
            print(f'O número {numero_1} é maior que o número {numero_2}')
        elif numero_1 == numero_2:
            print('Os dois números são semelhantes')
        else:
            print(f'O número {numero_2} é maior que o número {numero_1}')
    elif opcao == 4:
        print("Opção escolhida NOVOS NÚMEROS")
    elif opcao == 5:
        print("Opção escolhida SAIR")
        break
    else:
        print("Tente novamente")
print("FORA")
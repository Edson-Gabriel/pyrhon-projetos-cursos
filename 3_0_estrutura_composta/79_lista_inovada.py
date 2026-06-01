# Crie um programa onde o usuário possa digitar vários valores 
# numéricos e cadastre-os em uma lista. Caso o número já exista 
# lá dentro, ele não será adicionado. No final, serão exibidos 
# todos os valores únicos digitados, em ordem crescente. 

numeros = []
while True:

    while True:
        numero_novo = int(input("Informe um novo número: "))
        if numero_novo in numeros:
            print(f"Já existe o número {numero_novo}!")
        else:
            numeros.append(numero_novo)
            break

    opcao = " "
    while opcao not in "SN":
        opcao = input("Deseja continuar [S/N]? ").strip().upper()[0]
    if opcao in "N":
        break

print(sorted(numeros))
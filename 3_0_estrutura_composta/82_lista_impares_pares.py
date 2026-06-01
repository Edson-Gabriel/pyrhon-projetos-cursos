# Crie um programa que vai ler vários números e colocar em uma lista. 
# Depois disso, crie duas listas extras que vão conter apenas os 
# valores pares e os valores ímpares digitados, respectivamente. Ao 
# final, mostre o conteúdo das três listas geradas.


# Primeira versão feita por mim

numeros = []
impares = []
pares = []

while True:
    numero_novo = 0
    while True: #Validando que o numero informado seja diferente do que consta na lista
        numero_novo = int(input("Informe um novo número: "))
        if numero_novo in numeros:
            print(f"Já existe o número {numero_novo}!")
        else:
            numeros.append(numero_novo)
            break

    if numero_novo % 2 == 0: #Separando as listas dos pares
        pares.append(numero_novo)
    else: #Separando as listas dos impares
        impares.append(numero_novo)

    opcao = " " #Validando que o usuário digite a opção certa
    while opcao not in "SN":
        opcao = input("Deseja continuar [S/N]? ").strip().upper()[0]
    if opcao in "N":
        break

print(f"Os números digitados foram: {numeros}")
print(f"Os números pares digitados foram: {pares}")
print(f"Os números impares digitados foram: {impares}")

# Segunda versão adaptada do professor.
# Feito sem as validações dos números novos e opção digitada.

# numeros = []
# impares = []
# pares = []

# while True:
#     numero_novo = int(input("Informe um novo número: "))
#     if numero_novo in numeros:
#         print(f"Já existe o número {numero_novo}!")
#     else:
#         numeros.append(numero_novo)
#         break

#     opcao = input("Deseja continuar [S/N]? ").strip().upper()[0]
#     if opcao in "N":
#         break

# for i in numeros:
#     if i % 2 == 0:
#         pares.append(i)
#     else:
#         impares.append(i)

# print(f"Os números digitados foram: {numeros}")
# print(f"Os números pares digitados foram: {pares}")
# print(f"Os números impares digitados foram: {impares}")

# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

numeros_completos = []
while True:
    numeros_completos.append(int(input(f"Digite um número: ")))
    opcao = " "
    while opcao not in "SN":
        opcao = input("Deseja continuar [S/N]? ").strip().upper()[0]
    if opcao in "N":
        break
print(f"Você digitou {len(numeros_completos)} valores!")
print(f"Do menor para o maior: {sorted(numeros_completos, reverse=True)}")
if 5 in numeros_completos:
    print(f"O primeiro numero 5 foi digitado na posição {numeros_completos.index(5)+1}")
else:
    print(f"O número 5 não consta na lista: {numeros_completos}")
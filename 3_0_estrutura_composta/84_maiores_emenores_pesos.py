# Faça um programa que leia nome e peso de várias pessoas, 
# guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

pessoas_finais = []
total_pessoas = maior_peso = menor_peso = 0
nomes_maiores = nomes_menores = " "

while True:
    pessoas_finais.append([str(input("Nome: ")), float(input("Peso: "))])

    opcao = " "
    while opcao not in "SN":
        opcao = str(input("Deseja continuar? ")).strip().upper()[0]
    if opcao in "N":
        break

for nome, peso in pessoas_finais:
    total_pessoas += 1
    if total_pessoas == 1:
        maior_peso = menor_peso = peso
        nomes_maiores = [nome]
        nomes_menores = [nome]
    else:
        if peso > maior_peso:
            maior_peso = peso
            nomes_maiores = [nome]
        elif peso == maior_peso:
                nomes_maiores.append(nome)
        if peso < menor_peso:
            menor_peso = peso
            nomes_menores = [nome]
        elif peso == menor_peso:
            nomes_menores.append(nome)

print(f"Total de pessoas cadastradas: {total_pessoas}")
print(f"O maior peso foi de {maior_peso}Kg. Pertence a: {nomes_maiores}")
if nomes_maiores == nomes_menores:
    print(f"Todos com o mesmo peso ou somente um cadastro feito...")
else:
    print(f"O menor peso foi de {menor_peso}Kg. Pertence a: {nomes_menores}")
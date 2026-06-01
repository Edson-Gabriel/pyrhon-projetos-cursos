# Crie um programa onde o usuário possa digitar sete valores 
# numéricos e cadastre-os em uma lista única que mantenha 
# separados os valores pares e ímpares. No final, mostre os 
# valores pares e ímpares em ordem crescente.

lista = [[], []]
for i in range(7):
    i = int(input("Informe um valor: "))
    if i % 2 == 0:
        lista[0].append(i)
    else:
        lista[1].append(i)
print(f"Os números pares digitados foram os: {sorted(lista[0])}")
print(f"Os números impares digitados foram os: {sorted(lista[1])}")
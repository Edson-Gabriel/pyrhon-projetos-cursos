# Faça um programa que mostre a taabuada de multiplicação

numero = int(input("Digite o numero que voce quer saber da tabuada: "))
print('-' * 12)
for num_2 in range(11):
    resultado = numero * num_2
    print(f"{numero} X {num_2:2} = {resultado}")
print('-' * 12)

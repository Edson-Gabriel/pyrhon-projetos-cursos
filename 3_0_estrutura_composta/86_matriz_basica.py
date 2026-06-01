# Crie um programa que declare uma matriz de dimensão 3x3 e 
# preencha com valores lidos pelo teclado. No final, mostre 
# a matriz na tela, com a formatação correta.

matriz_final = [[], [], []]

for linha in range(3):
    for coluna in range(3):
        valor = int(input(f"Digite o valor_1 para [{linha}, {coluna}]: "))
        matriz_final[linha].append(valor)

print("-" * 30)
for linha in range(3):
    for coluna in range(3):
        print(f"[{matriz_final[linha][coluna]:^5}]", end=" ")
    print()
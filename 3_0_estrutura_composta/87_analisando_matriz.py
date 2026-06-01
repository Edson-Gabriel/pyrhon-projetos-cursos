# Aprimore o desafio anterior, mostrando no final: 
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

matriz_final = [[], [], []]
pares = soma_coluna = maior_valor_2 = 0
for linha in range(3):
    for coluna in range(3):
        valor = int(input(f"Digite o valor_1 para [{linha}, {coluna}]: "))
        matriz_final[linha].append(valor)
        if valor % 2 == 0:
            pares += valor
print("-" * 30)
for linha in range(3):
    for coluna in range(3):
        print(f"[{matriz_final[linha][coluna]:^5}]", end=" ")
    print()


print(sum(coluna[2] for coluna in matriz_final))
print(max(matriz_final[1]))
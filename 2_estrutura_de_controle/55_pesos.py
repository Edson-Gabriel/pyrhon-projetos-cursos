# Vendo o maior e menor peso

peso_maior = 0
peso_menor = 0
for i in range (5):
    peso = float(input(f"Informe o peso da {i+1}º pessoa em kg: "))
    if i == 0:
        peso_maior = peso
        peso_menor = peso
    else:
        if peso > peso_maior:
            peso_maior = peso
        if peso < peso_menor:
            peso_menor = peso
print(f"O maior peso foi {peso_maior}kg")
print(f"O menor peso foi {peso_menor}kg")
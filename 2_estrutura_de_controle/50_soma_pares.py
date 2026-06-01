# Somando os números pares e números impares

pares_numeros = 0
impares_numeros = 0
for i in range (6):
    numero = int(input("Informe um número inteiro: "))
    if numero % 2 == 0:
        print(f"Número par {numero}")
        pares_numeros += numero
    else:
        print(f"Número impar {numero}")
        impares_numeros += numero
print(f"O resultado da soma dos números pares foi de: {pares_numeros}")
print(f"O resultado da soma dos números impares foi de: {impares_numeros}")

# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.

numeros = ((int(input("Informe o primeiro número: "))), (int(input("Informe o segundo número: "))), (int(input("Informe o terceiro número: "))), (int(input("Informe o quarto número: "))))
print(numeros)
print(f"O valor 9 apareceu {numeros.count(9)}", "vez" if numeros.count(9) == 1 else "vezes")
print(f"O valor 3 foi digitado na {numeros.index(3)+1}º posição" if 3 in numeros else "O valor 3 não foi digitado em nenhuma posição.")
print("Os valores pares digitados foram: ", end="")
print(tuple(i for i in numeros if i % 2 == 0))

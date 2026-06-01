# comparando valores

from random import randint

numero_1 = randint(0,10)
numero_2 = randint(0,10)
numero_3 = randint(0,10)
print(f"Número 1: {numero_1}")
print(f"Número 2: {numero_2}")
print(f"Número 3: {numero_3}")
print(f"O maior número é {max(numero_1, numero_2, numero_3)}") # Usando o método max  para comparar os valores
print(f"O menor número é {min(numero_1, numero_2, numero_3)}") # Usando o método min para comparar os valores



# Usando estrutras de condições para comparar os valores, e informar qual é o maior e menor


# from random import randint

# numero_1 = randint(0,10)
# numero_2 = randint(0,10)
# numero_3 = randint(0,10)
# if numero_1 > numero_2 and numero_1 > numero_3:
#     maior = numero_1
#     if numero_2 < numero_3:
#         menor = numero_2
#     else:
#         menor = numero_3
# if numero_2 > numero_1 and numero_2 > numero_3:
#     maior = numero_2
#     if numero_1 < numero_3:
#         menor = numero_1
#     else:
#         menor = numero_3
# if numero_3 > numero_2 and numero_3 > numero_1:
#     maior = numero_3
#     if numero_2 < numero_1:
#         menor = numero_2
#     else:
#         menor = numero_1
# print(f"Número 1: {numero_1}")
# print(f"Número 2: {numero_2}")
# print(f"Número 3: {numero_3}")
# print(maior)
# print(menor)


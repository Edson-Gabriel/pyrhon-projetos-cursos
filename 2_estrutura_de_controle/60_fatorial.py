#Faça um programa que leia um número qualquer e mostre o seu fatorial

from math import factorial

fatorial = int(input("Informe o número para descobrir o fatorial: "))
contador = fatorial
while contador > 0:
    print(f"{contador}", end=" x " if contador > 1 else " = ")
    contador-=1
print(factorial(fatorial))
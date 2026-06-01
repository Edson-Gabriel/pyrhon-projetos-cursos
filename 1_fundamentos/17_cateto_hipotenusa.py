# Faça um programa que calcule a Hipotenusa com módulos

from math import hypot
cateto_oposto = float(input("Informe o cateto oposto: "))
cateto_adjacente = float(input("Informe o cateto adjacente: "))
hipotenusa = hypot(cateto_adjacente, cateto_oposto)
print(f"{hipotenusa:.2f}")
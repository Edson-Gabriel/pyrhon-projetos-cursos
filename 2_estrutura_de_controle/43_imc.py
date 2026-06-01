# Faça um programa que calcule o IMC

altura = int(input("Informe sua altura em cm: "))
peso = float(input("Informe seu peso em KG: "))
imc = peso / ((altura / 100)**2)
print(f"{imc:.2f}")
if imc < 18.5:
    print("Abaixo do peso")
elif imc >= 18.5 and imc < 25:
    print("Peso ideal")
elif imc >= 25 and imc < 30:
    print("Sobrepeso")
elif imc >= 30 and imc <= 40:
    print("Obesidade")
else:
    print("Obesidade mórbida")
# Comparando dois números inteiros

numero_1 = int(input("Digite o primeiro valor: "))
numero_2 = int(input("Digite o segundo valor: "))
if numero_1 > numero_2:
    print(f"O primeiro valor informado é maior que o segundo: {numero_1} e {numero_2}")
elif numero_1 < numero_2:
    print(f"O segundo valor informado é maior que o primeiro: {numero_2} e {numero_1}")
else:
    print("Ambos são idênticos")
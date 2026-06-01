# Faça um programa que leias as notas do aluno e informe se ele 
# esta aprovado, recuperação ou reprovado

nota_1 = float(input("Informe sua primeira nota: "))
nota_2 = float(input("Informe sua segunda nota: "))
media = (nota_1 + nota_2) / 2
print(f"{media:.2f}")
if media < 5:
    print("Reprovado!")
elif media >= 7:
    print("Aprovado!")
else:
    print("Recuperação!")
print("Bons Estudos!")
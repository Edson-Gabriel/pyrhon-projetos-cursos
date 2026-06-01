# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. 
# Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = input("Informe o gênero [M/F] ").upper().strip()
while not sexo == "M" and not sexo == "F":
    sexo = input("Informe o sexo [M/F]: ").upper().strip()
print("Registro concluido!")

# while True:
#     sexo = str(input('Digite o sexo [M/F]: ')).upper().strip()
#     if sexo == 'M':
#         print('Homem')
#         break
#     elif sexo == 'F':
#         print('Mulher')
#         break
#     else:
#         print('TENTE NOVAMENTE')
# print('Aacbou')
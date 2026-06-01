# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
# No final, mostre: 
# Quantas pessoas tem mais de 18 anos;
# Quantos homens foram cadastrados;
# Quantas mulheres tem menos de 20 anos.

maior_18 = homens = mulheres_20 = 0
while True:
    print("=:" * 25)
    idade = int(input("Informe a idade: "))
    
    if idade >= 18:
        maior_18 += 1
    
    sexo = ' '
    while sexo not in "MmFf":
        sexo = str(input("Informe o sexo [M/F]: ")).strip().upper()[0]
    if sexo in "M":
        homens += 1
    elif sexo in "F" and idade <= 20:
        mulheres_20 += 1
    print('*'*25)
    opcao = ' '
    while opcao not in "SsNn":
        opcao = input("Deseja continuar [S/N]: ").strip().upper()[0]
    if opcao == "N":
        break

print(f"\nExiste {maior_18} pessoas maiores de 18 anos.")
print(f"{homens} homens foram encontrados.")
print(f"Existe {mulheres_20} mulheres abaixo de 20 anos.")
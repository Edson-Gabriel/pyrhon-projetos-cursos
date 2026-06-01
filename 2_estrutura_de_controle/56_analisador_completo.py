#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. 
# No final do programa, mostre: a média de idade do grupo, 
# qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

nome_homem = ""
idade_homem = 0
total_mulheres = 0
idade_grupo = 0
media_idade = 0
for i in range (4):
    nome = input(f"Informe o {i+1}º nome: ")
    idade = int(input(f"Informe a idade do {nome}: "))
    sexo = input("Informe o sexo [M/F]: ").upper().strip()
    
    idade_grupo += idade

    if sexo == "M" and  idade > idade_homem:
            nome_homem = nome
            idade_homem = idade
    elif sexo == "F" and idade < 20:
            total_mulheres +=1
    else:
        print("SEXO INVÁLIDO!")
    
media_idade = idade_grupo / 3 
print(f"A média da idade do grupo é de {media_idade:.2f} anos")
if idade_homem != -1:
    print(f"O homem mais velho se chama {nome_homem}, ele tem {idade_homem} anos")
else:
      print("Nenhum homem registrado ""teste"" ")
if total_mulheres != 0:
    print(f"Tem um total de {total_mulheres} com menos de 20 anos")
else:
     print("Nenhuma mulher acima de 20 anos ou nenhuma mulher registrada.")
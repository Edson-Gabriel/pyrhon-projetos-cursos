# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: 
# A) Quantas pessoas foram cadastradas
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média

ficha_cadastro = {}
cadastros_concluidos = []
soma_idade = 0
while True:
    ficha_cadastro['nome'] = str(input("NOME: "))
    while True:
        ficha_cadastro['sexo'] = str(input("SEXO: [M/F]  ")).upper().strip()[0]
        if ficha_cadastro['sexo'] in "MF":
            break
        print('Erro! Responda com "F" para FEMININO, ou "M" para MASCULINO')

    ficha_cadastro['idade'] = int(input("IDADE: "))
    soma_idade += ficha_cadastro['idade']

    cadastros_concluidos.append(ficha_cadastro.copy())
    
    while True:
        opcao = input("Quer continuar? [S/N] ").upper().strip()[0]
        if opcao in "SN":
            break
        print('ERRO! Digite somente "S" para sim, ou "N" para não')
    if opcao in "N":
        break
print("-="*50)
print(f"{"A )":<4} Ao todo temos {len(cadastros_concluidos)} pessoas cadastradas.")
media = soma_idade / len(cadastros_concluidos)
print(f"{"B )":<4} A média de idades é de {media:.2f} anos.")
print(f"{"C )":<4} As mulheres cadastradas foram: ", end=" ")
for mulheres in cadastros_concluidos:
    if mulheres['sexo'] in "F":
        print(mulheres['nome'], end=": ")
print(f"\n{"D )":<4} Lista das pessoas que estão acima da média:")
for pessoas in cadastros_concluidos:
    if pessoas['idade'] >= media:
        for keys, valor in pessoas.items():
            print(f"     {keys} = {valor}", end=" ")
print("<ENCERRADO>")
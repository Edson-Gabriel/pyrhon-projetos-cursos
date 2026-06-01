# Crie um programa que leia nome e duas notas de vários alunos 
# e guarde tudo em uma lista composta. No final, mostre um 
# boletim contendo a média de cada um e permita que o usuário 
# possa mostrar as notas de cada aluno individualmente.

boletim = []

while True:
    alunos = input("Digite o nome do aluno: ")
    nota_1 = float(input("Digite a nota 1: "))
    nota_2 = float(input("Digite a nota 2: "))
    media_notas = (nota_1 + nota_2) / 2
    boletim.append([alunos, [nota_1, nota_2, media_notas]])

    opcao = " "
    while opcao not in "SN":
        opcao = input("Deseja continuar? [S/N] ").upper().strip()[0]
    if opcao in "N":
        break

print("-="*50)
print(f"{'Nº.':<4}{'NOME':<15}{'MEDIA':>5}")

for indice, alunos in enumerate(boletim):
    nomes = alunos[0]
    medias = alunos[1][2]
    print(f"{indice:<4}{nomes:<15}{medias:>5}")

while True:
    escolha_o_aluno = int(input("Você deseja ver a nota de qual aluno(a)? [999 para interromper] "))
    if escolha_o_aluno == 999:
        break
    else:
        print(f"As notas do(a) {boletim[escolha_o_aluno][0]}, foram {boletim[escolha_o_aluno][1][0]:.2f} e {boletim[escolha_o_aluno][1][1]:.2f} ")
    
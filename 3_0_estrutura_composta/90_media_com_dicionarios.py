# Faça um programa que leia nome e média de um aluno, 
# guardando também a situação em um dicionário. 
# No final, mostre o conteúdo da estrutura na tela.

registro_turma = [] 
ficha_aluno = {}
while True:
    ficha_aluno["nome"] = input("Nome: ").strip().upper()
    ficha_aluno["notas"] = [(float(input("Nota 1: "))), (float(input("Nota 2: ")))]
    ficha_aluno["media"] = sum(ficha_aluno["notas"]) / 2
    if ficha_aluno["media"] >=6:
        ficha_aluno["situacao"] = "Aprovado"
    else:
        ficha_aluno["situacao"] = "Reprovado"
    registro_turma.append(ficha_aluno.copy())
    opcao = " "
    while opcao not in "SN":
        opcao = input("Deseja continuar? [S/N] ").upper().strip()[0]
    if opcao in "N":
        break
print(f"{"FICHA ALUNOS":-^52}")
print(f"{'Nº.':<4}{'NOME':<15}{'MEDIA':>5}{"SITUAÇÃO":>15}")
for i, v in enumerate(registro_turma):
    print(f"{i:<4}{registro_turma[i]["nome"]:<15}{registro_turma[i]["media"]:>5}{registro_turma[i]["situacao"]:>15}")
while True:
    escolha_o_aluno = int(input("Você deseja ver a nota de qual aluno(a)? [999 para interromper] "))
    aluno_selecionado = registro_turma[escolha_o_aluno]
    if escolha_o_aluno == 999:
        break 
    else:
        print(f"As notas do(a) {aluno_selecionado['nome']}, foram {aluno_selecionado['notas'][0]:.2f} {aluno_selecionado['notas'][1]:.2f}")
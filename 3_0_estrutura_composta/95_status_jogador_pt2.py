# Aprimore o desafio 93 para que ele funcione com vários jogadores, 
# incluindo um sistema de visualização de detalhes do aproveitamento 
# de cada jogador.

status_jogadores = []
ficha_jogador = {}
while True:
    ficha_jogador['nome'] = str(input("Informe o nome do jogador: ")).upper().strip()
    ficha_jogador['partidas_jogadas'] = int(input(f"Informe quantas partidas o jogador {ficha_jogador['nome']}, jogou: "))

    print("-="*50)
    gols_partidas = []
    for jogos in range (ficha_jogador['partidas_jogadas']):
        gols_partidas.append(int(input(f"    Quantos gol o jogador marcou na {jogos+1}º partida: ")))
    ficha_jogador['gols'] = gols_partidas.copy()
    ficha_jogador['total_gols'] = sum(ficha_jogador['gols'])
    print("-="*50)

    status_jogadores.append(ficha_jogador.copy())

    while True:
        opcao = input(f"Quer continuar? [S/N] ").upper().strip()[0]
        if opcao in "SN":
            break
        print("Erro! S para sim, ou N para não")
    if opcao in "N":
        break

while True:
    print("-="*50)
    print(f"{'Nº.':<4}{'JOGADOR':<15}{'GOLS':<15}{'TOTAL DE GOLS':>15}")
    for indice, valor in enumerate(status_jogadores):
        print(f"{indice:<4}{valor['nome']:<15}{str(valor['gols']):<15}{valor['total_gols']:>15}")

    print("-="*50)

    opcao = int(input("Informe o jogador que deseja ver as estáticas [999 para parar]: "))
    
    print("-="*50)

    if opcao == 999:
        break
    elif opcao >= len(status_jogadores) or opcao < 0:
        print("ERRO! Digite somente o Nº do jogador desejado.")
    else:
        print(f"Estatisticas do jogador: {status_jogadores[opcao]['nome']}")
        for partidas, gols in enumerate(status_jogadores[opcao]['gols']):
            print(f"No jogo {partidas+1}, fez {gols} gols.")
print("-="*50)
print("Obrigado por usar nosso sistema de estátisticas!")
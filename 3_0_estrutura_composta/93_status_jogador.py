# Crie um programa que gerencie o aproveitamento de um 
# jogador de futebol. O programa vai ler o nome do jogador 
# e quantas partidas ele jogou. Depois vai ler a quantidade 
# de gols feitos em cada partida. No final, tudo isso será 
# guardado em um dicionário, incluindo o total de gols 
# feitos durante o campeonato.

ficha_jogador = {}
gols_partidas = []
ficha_jogador['nome'] = str(input("Informe o nome do jogador: "))
ficha_jogador['partidas_jogadas'] = int(input(f"Informe quantas partidas o jogador {ficha_jogador['nome']}, jogou: "))

#usando List Comprehension, porém ficou menos legível
# ficha_jogador["gols"] = [int(input(f"Quantos gols o {ficha_jogador['nome']} marcou no {jogos+1}º jogo: ")) for jogos in range(ficha_jogador['partidas_jogadas'])] 

print("-="*50)
# Usando for "padrao". Mais linhas, porém mais legível
for jogos in range (ficha_jogador['partidas_jogadas']):
    gols_partidas.append(int(input(f"    Quantos gol o jogador marcou na {jogos+1}º partida: ")))
ficha_jogador['gols'] = gols_partidas.copy()
ficha_jogador['total_gols'] = sum(ficha_jogador['gols'])
print("-="*50)

print(ficha_jogador)

print("-="*50)
for keys, valor in ficha_jogador.items():
    print(f"O campo {keys}, tem o valor {valor}")
print("-="*50)

print(f"O jogador {ficha_jogador['nome']}, jogou {ficha_jogador['partidas_jogadas']} partidas.")
for jogos in range(ficha_jogador['partidas_jogadas']):
    print(f"    => Na {jogos+1}º partida, marcou {ficha_jogador['gols'][jogos]} gols!" if ficha_jogador['gols'][jogos] != 1 else 
        f"    => Na {jogos+1}º partida, marcou {ficha_jogador['gols'][jogos]} gol!")
print(f"Foi um total de {ficha_jogador['total_gols']} gols" if ficha_jogador['total_gols'] != 1 else f"Marcou apenas {ficha_jogador['total_gols']} gol")
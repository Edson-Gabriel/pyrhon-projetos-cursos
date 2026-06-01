# Faça um programa que tenha uma função chamada ficha(), que 
# receba dois parâmetros opcionais: o nome de um jogador e 
# quantos gols ele marcou. O programa deverá ser capaz de mostrar 
# a ficha do jogador, mesmo que algum dado não tenha sido 
# informado corretamente.

def ficha(nome = "<desconhecido>", gols = 0):
    return f"O jogador {nome} fez {gols} gol(s) no campeonato"

nome_jogador = input("Nome JOGADOR: ")
gols_jogador = input("Número de GOLS: ")
if gols_jogador.isnumeric():
    gols_jogador = int(gols_jogador)
else:
    gols_jogador = 0

if nome_jogador.strip()== "":
    print(ficha(gols=gols_jogador))
else:
    print(ficha(nome_jogador, gols_jogador))
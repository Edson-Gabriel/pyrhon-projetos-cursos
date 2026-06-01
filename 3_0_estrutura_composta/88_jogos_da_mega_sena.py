#Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 
# 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma 
# lista composta.

from random import randint
jogos_mega_sena = []
quantidade_de_jogos = int(input("Quantos jogos você quer fazer? "))
for i in range(quantidade_de_jogos):
    temporario = []
    while len(temporario) < 6:
        numero = randint(1,60)
        if numero not in temporario:
            temporario.append(numero)
    temporario.sort()
    jogos_mega_sena.append(temporario.copy()) 
for quantia in range(len(jogos_mega_sena)):
    print(jogos_mega_sena[quantia])
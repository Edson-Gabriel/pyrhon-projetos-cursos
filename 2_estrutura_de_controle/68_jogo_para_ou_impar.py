# Faça um programa que jogue par ou ímpar com o computador. O jogo só 
# será interrompido quando o jogador perder, mostrando o total de 
# vitórias consecutivas que ele conquistou no final do jogo.

from random import randint
vitorias = 0
while True:
    computador = randint(0, 10)
    jogador = int(input("Escolha um número: "))
    total_jogado = jogador + computador
    impar_par = ' '
    while impar_par not in "IP":
        impar_par = input("Impar ou Par [I/P]: ").strip().upper()[0]
        print("Escolha somente IMPAR ou PAR")
    print(f"Você jogou {jogador} e o computador {computador}. Total de {total_jogado}", end=" ")
    print("Deu PAR" if total_jogado % 2 == 0 else "Deu IMPAR" )
    if total_jogado % 2 == 0:
        if impar_par == "P":
            print("Você venceu!\nVamos jogar novamente...")
            vitorias += 1
        else:
            print("Você perdeu...")
            break
    else:
        if impar_par == "I":
            print("Você venceu!\nVamos jogar novamente...")
            vitorias += 1
        else:
            print("Você perdeu...")
            break
print(f"Você conseguiu {vitorias} consecutivas.")
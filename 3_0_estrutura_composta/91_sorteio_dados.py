# Crie um programa onde 4 jogadores joguem um dado e 
# tenham resultados aleatórios. Guarde esses resultados 
# em um dicionário em Python. No final, coloque esse 
# dicionário em ordem, sabendo que o vencedor tirou o 
# maior número no dado.

from random import randint
from time import sleep
from operator import itemgetter
jogadores = {
    'jogador1': randint(1,6),
    'jogador2': randint(1,6),
    'jogador3': randint(1,6),
    'jogador4': randint(1,6)
}
print("Valores sorteados:")
for i, v in jogadores.items():
    print(f"O {i}, tirou {v}")
    sleep(1)
print(f"{sorted(jogadores)}")
ranking  = sorted(jogadores.items(), key= itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f"{i+1}º lugar para o {v[0]} com {v[1]} ")
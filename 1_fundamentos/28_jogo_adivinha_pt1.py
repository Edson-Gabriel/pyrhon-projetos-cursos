# Adivinhando o número que o computador sorteae

import random

pensamento_computador = random.randint(0, 5)
palpite = int(input("Digite o seu palpite (0-5): "))
if palpite == pensamento_computador:
    print("Você acertou!!!")
else:
    print("Infelizmente você errou...")

# Adivinhando o número que o computador sorteia

import random

pensamento_computador = random.randint(0, 5)
total_palpites = 0
while True:
    total_palpites += 1
    palpite = int(input("Digite o seu palpite (0-5): "))
    if palpite == pensamento_computador:
        print("Você acertou!!!")
        break
    else:
        print("Infelizmente você errou tenta de novo...")
print(f"Parabéns você acertou na tentativa {total_palpites}")

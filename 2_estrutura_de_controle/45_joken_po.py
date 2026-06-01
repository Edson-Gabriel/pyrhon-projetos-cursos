# Faça um programa que jogue JOKENPO

from random import choice
usuario = input("Escolha pedra, papel ou tesoura: ").upper()
maquina = ["PEDRA", "PAPEL", "TESOURA"]
maquina = choice(maquina)
print(f"Você jogou {usuario} e a maquina {maquina}")
print("Resultado:")

if maquina == "PEDRA":
    if usuario == "Pedra".upper():
        print("Empate")
    elif usuario == "papel".upper():
        print("Vitória!")
    elif usuario == "Tesoura".upper():
        print("Derrota")
    else:
        print("invalido")

elif maquina == "PAPEL":
    if usuario == "Pedra".upper():
        print("Derrota")
    elif usuario == "papel".upper():
        print("Empate!")
    elif usuario == "Tesoura".upper():
        print("Vitória")
    else:
        print("invalido")

else: 
    if usuario == "Pedra".upper():
        print("Vitória")
    elif usuario == "papel".upper():
        print("Derrota!")
    elif usuario == "Tesoura".upper():
        print("Empate")
    else:
        print("invalido")



# Código 2
# import random

# maquina = random.randint(1, 3)
# usuario = input("Escolha pedra, papel ou tesoura: ").upper() 
# if maquina == 1:
#      maquina_escolha = "Pedra"
# elif maquina == 2:
#     maquina_escolha = "Papel"
# else:
#     maquina_escolha = "Tesoura"

# print(f"Você jogou {usuario} e a maquina {maquina_escolha}")
# print("Resultado:")

# if maquina == 1 and usuario == "Pedra".upper():
#     print("Empate")
# elif maquina == 1 and usuario == "Papel".upper():
#     print("Vitória")
# elif maquina == 1 and usuario == "Tesoura".upper():
#     print("Derrota")
# elif maquina == 2 and usuario == "Pedra".upper():
#     print("Derrota")
# elif maquina == 2 and usuario == "Papel".upper():
#     print("Empate")
# elif maquina == 2 and usuario == "Tesoura".upper():
#     print("Vitoria")
# elif maquina == 3 and usuario == "Pedra".upper():
#     print("Vitória")
# elif maquina == 3 and usuario == "Papel".upper():
#     print("Derrota")
# elif maquina == 3 and usuario == "Tesoura".upper():
#     print("Empate")
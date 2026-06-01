# Faça um mini-sistema que utilize o Interactive Help do Python. 
# O usuário vai digitar o comando e o manual vai aparecer. 
# Quando o usuário digitar a palavra 'FIM', o programa se 
# encerrará.

def ajuda(com):
    titulo(f"Acessando o manual do comando \'{com}\'")
    help(com)

def titulo(msg):
    tam = len(msg) + 4
    print("~"* tam)
    print(f"    {msg}")
    print("~"* tam)


comando = ''
while True:
    titulo("SISTEMA DE AJUDA PyGB")
    comando = input("Função ou biblioteca -> ")
    if comando.upper() == "FIM":
        break
    else:
        ajuda(comando)
titulo("ATÉ LOGO!")
# Melhore o DESAFIO 061, perguntando para o usuário se ele quer
# mostrar mais alguns termos. O programa encerrará quando ele 
# disser que quer mostrar 0 termos.

while True:
    primeiro_termo = int(input('Digite o primeiro termo: '))
    razao = int(input('Digite a razão: '))
    contagem = 0
    for i in range (10):
        termo = razao * i + primeiro_termo
        print(termo)
    sair = input("Deseja sair? S/N ").upper().strip()
    if sair == "S":
        break
    else:
        continue
# Faça um programa que tenha uma função chamada contador(), que 
# receba três parâmetros: início, fim e passo. Seu programa tem 
# que realizar três contagens através da função criada:

# a) de 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2
# c) uma contagem personalizada

from time import sleep

def contagem_personalizada(a, b, c):
    if c == 0:
        c = 1 if a < b else -1
    if (a > b and c > 0) or (a < b and c < 0):
        c = -c
    for i in range (a, b, c):
        print(i, end=" ", flush= True)
        sleep(0.5)
    print()


print("-----CONTAGEM 1 A 10-----")
contagem_personalizada(1, 11, 1)
print("-----CONTAGEM 10 A 1-----")
contagem_personalizada(10, 0, -1)
print("-----CONTAGEM PERSONALIZADA----")
contagem_personalizada(    
int(input("Inicio:  ")),
int(input("Final:   ")),
int(input("Passo:   ")))
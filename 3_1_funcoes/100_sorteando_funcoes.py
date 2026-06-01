# Faça um programa que tenha uma lista chamada números 
# e duas funções chamadas sorteia() e somaPar(). A primeira 
# função vai sortear 5 números e vai colocá-los dentro da 
# lista e a segunda função vai mostrar a soma entre todos os 
# valores pares sorteados pela função anterior.

import random
from time import sleep
def sorteio():
    numeros = []
    valores_pares = 0
    print("Sorteando os 5 valores da lista: ", end="")
    for i in range(5):
        i = random.randint(0, 11)
        print(i, end=' ')
        sleep(0.3)
        if i % 2 ==0:
            valores_pares += i
        numeros.append(i)
    print("Pronto!")
    sleep(0.5)
    print(f"Somando os valores pares de {numeros}, temos {valores_pares}")

sorteio()
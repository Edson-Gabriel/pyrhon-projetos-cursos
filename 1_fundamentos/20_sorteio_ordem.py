# Faça um programa que sorteia um nome para começar a apresentação

import random
nome1 = input("Digite seu nome (01): ")
nome2 = input("Digite seu nome (02): ")
nome3 = input("Digite seu nome (03): ")
nome4 = input("Digite seu nome (04): ")
lista_alunos = [nome1, nome2, nome3, nome4]
random.shuffle(lista_alunos)
print(lista_alunos)
# Faça um programa que sorteia os nomes
import random
nome1 = input("Digite seu nome (01): ")
nome2 = input("Digite seu nome (02): ")
nome3 = input("Digite seu nome (03): ")
nome4 = input("Digite seu nome (04): ")
lista_alunos = [nome1, nome2, nome3, nome4]
nome_sorteado = random.choice(lista_alunos)
print(nome_sorteado)
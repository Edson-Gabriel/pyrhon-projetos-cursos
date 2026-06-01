#  Crie um programa que vai gerar cinco números aleatórios e 
# colocar em uma tupla. Depois disso, mostre a listagem de 
# números gerados e também indique o menor e o maior valor que 
# estão na tupla.

from random import randint
tupla_aleatoria = tuple(randint(1, 100) for i in range(5))
print(f"Tupla gerada: {tupla_aleatoria}")
print(f"o maior número gerado foi o: {max(tupla_aleatoria)}")
print(f"O menor número gerado foi o:  {min(tupla_aleatoria)}")
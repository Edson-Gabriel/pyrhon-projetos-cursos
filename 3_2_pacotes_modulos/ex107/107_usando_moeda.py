# Crie um módulo chamado moeda.py que tenha as funções 
# incorporadas aumentar(), diminuir(), dobro() e metade(). 
# Faça também um programa que importe esse módulo e use 
# algumas dessas funções.

import moeda_107
p = float(input("Digite um valor: "))
print(f"Aumentando 15% em cima do {p}, fica {moeda_107.aumentar(p, 15)}")
print(f"Diminuindo 15% em cima do {p}, fica {moeda_107.diminuir(p, 15)}")
print(f"Dobro de {p}, é {moeda_107.dobrando(p)}")
print(f"Metade de {p}, é {moeda_107.metade(p)}")
# Adapte o código do desafio #107, criando uma função adicional 
# chamada moeda() que consiga mostrar os números como um valor 
# monetário formatado.

import moeda_108

p = float(input("Digite um valor: "))
print(f"Aumentando 15% em cima do {moeda_108.moeda(p)}, fica {moeda_108.moeda(moeda_108.aumentar(p, 15))}")
print(f"Diminuindo 15% em cima do {moeda_108.moeda(p)}, fica {moeda_108.moeda(moeda_108.diminuir(p, 15))}")
print(f"Dobro de {moeda_108.moeda(p)}, é {moeda_108.moeda(moeda_108.dobrando(p))}")
print(f"Metade de {moeda_108.moeda(p)}, é {moeda_108.moeda(moeda_108.metade(p))}")
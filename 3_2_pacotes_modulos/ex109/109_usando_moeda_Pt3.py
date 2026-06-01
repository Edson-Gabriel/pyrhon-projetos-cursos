# Modifique as funções que form criadas no desafio 107 para que 
# elas aceitem um parâmetro a mais, informando se o valor 
# retornado por elas vai ser ou não formatado pela função moeda(), 
# desenvolvida no desafio 108.


import moeda_109
p = float(input("Digite um valor: "))
print(f"Aumentando 15% em cima do {moeda_109.moeda(p)}, fica {moeda_109.aumentar(p, 15, True)}")
print(f"Diminuindo 15% em cima do {moeda_109.moeda(p)}, fica {moeda_109.diminuir(p, 15)}")
print(f"Dobro de {moeda_109.moeda(p)}, é {moeda_109.dobrando(p, True)}")
print(f"Metade de {moeda_109.moeda(p)}, é {moeda_109.metade(p)}")
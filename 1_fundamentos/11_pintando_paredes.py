# Faça um programa que use 3 informações para chegar no resultado final

largura_parede = float(input("Qual a largura da paredes em METROS "))
altura_parede = float(input("Qual a altura da paredes em METROS "))
area = largura_parede * altura_parede
tinta_parede = area / 2 #A cada 2m da parede, precisa de 1L de tinta
print(f"Sua parede tem a dimensão {largura_parede}m X {altura_parede}m e sua área é de {area}m²")
print(f"Vamos precisar de {tinta_parede}L de tinta")
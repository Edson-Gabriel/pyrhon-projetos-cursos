# Faça um programa que calcule os descontos

preco_normal = int(input("Qual o preço informado na etiqueta R$"))
preco_desconto = preco_normal - (preco_normal * 0.05)
print(f"O preço original do produto é de {preco_normal:.2f} com desconto fica por R${preco_desconto:.2f}")
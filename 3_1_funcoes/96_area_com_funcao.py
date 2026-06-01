# Faça um programa que tenha uma função chamada área(), 
# que receba as dimensões de um terreno retangular 
# (largura e comprimento) e mostre a área do terreno.

def area_terreno(a, b):
    area_total = a * b
    print(f"A área do terreno {a:.1f}x{b:.1f} é de {area_total}m²")

print(f"{"CONTROLE TERRENOS":^30}")
print("-"*40)

area_terreno(
    float(input("Largura (m): ")),
    float(input("Comprimento (m): "))
)
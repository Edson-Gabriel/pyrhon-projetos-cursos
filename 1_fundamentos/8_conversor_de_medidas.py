# Faça um programa que converta as medidas informadas

metros = float(input("Digite uma distância em metros: "))
km = metros / 1000
hm = metros / 100
dam = metros / 10
dm = metros * 10
cm = metros * 100
mm = metros * 1000

print(f"A medida de {metros:.2f}m corresponde a...")
print(f"{km:.2f}km")
print(f"{hm:.2f}hm")
print(f"{dam:.2f}dam")
print(f"{dm:.2f}dm")
print(f"{cm:.2f}cm")
print(f"{mm:.2f}mm")
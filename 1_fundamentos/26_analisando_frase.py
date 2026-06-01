# Analisando uma frase

frase = "Uma frase impactante".upper().strip()
print(f'A letra "A", aparece {frase.count("A")}x')
print(f'A primeira letra "A", esta na posição: {frase.find("A") + 1}')
print(f'A última letra "A", esta na posição: {frase.rfind("A") + 1}')

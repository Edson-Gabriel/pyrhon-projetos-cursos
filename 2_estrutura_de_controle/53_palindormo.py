# Verificando frases palíndromas

frase = "Arara arara arara".strip().upper()
frase_lista = frase.split()
frase_junta = "".join(frase_lista)
frase_inversa = frase_junta[::-1]
print(f"A frase escolhida é (sem espaços): {frase_junta}.\nO inverso da frase é (sem espaços): {frase_inversa}")
if frase_inversa == frase_junta:
    print("É um palíndromo")
else:
    print("Não é um palíndromo")
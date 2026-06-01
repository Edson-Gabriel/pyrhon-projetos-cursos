#Crie um programa que tenha uma tupla com várias palavras (não usar 
# acentos). Depois disso, você deve mostrar, para cada palavra, quais 
# são as suas vogais.

palavras_tuplas = "Aprender", "Programar", "Linguagem", "Curso"
for palavras in palavras_tuplas:
    print(f"\nNa palavra {palavras.upper()}, temos as avogais: ", end=" ")
    for vogais in palavras:
        if vogais.lower() in "aeiou":
            print(vogais, end=" ")
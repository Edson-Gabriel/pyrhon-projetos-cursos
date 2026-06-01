# Faça um programa que tenha uma função chamada escreva(), que 
# receba um texto qualquer como parâmetro e mostre uma mensagem 
# com tamanho adaptável.

def escrevendo_adaptado(msg):
    tamanho_texto = len(msg) + 4
    print("-"*tamanho_texto)
    print(f"  {msg}")
    print("-"*tamanho_texto)

escrevendo_adaptado(
    input("Texto/Frase: ")
)
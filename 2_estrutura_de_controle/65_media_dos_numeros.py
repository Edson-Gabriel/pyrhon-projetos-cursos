# Crie um programa que leia vários números inteiros pelo teclado. 
# No final da execução, mostre a média entre todos os valores e 
# qual foi o maior e o menor valores lidos. O programa deve perguntar 
# ao usuário se ele quer ou não continuar a digitar valores.

contador = numero_maior = numero_menor = media = soma = 0
resposta = "S"
while resposta in "S":
    contador += 1
    numero = int(input("Digite 1 numero: "))
    if contador == 1:
        numero_maior = numero_menor = numero
    else:
        if numero > numero_maior:
            numero_maior = numero
        elif numero < numero_menor:
            numero_menor = numero
    soma += numero
    resposta = input("Quer continuar [S/N]: ").upper()
media = soma/contador
print(f"A média dos números informados: {media:.2f}")
print(f"Número maior informado: {numero_maior}")
print(f"Número menor informado: {numero_menor}")
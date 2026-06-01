# Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, 
# que é a condição de parada. No final, mostre quantos números 
# foram digitados e qual foi a soma entre eles (desconsiderando o flag).

numero = 0  
numero_total = 0
while numero != 999:
    numero = int(input("Digite 1 número: "))
    if numero != 999:
        numero_total += numero
print(f"a soma dos números digitados: {numero_total}")
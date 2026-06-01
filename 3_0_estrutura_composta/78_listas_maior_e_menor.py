# Faça um programa que leia 5 valores numéricos e guarde-os em 
# uma lista. No final, mostre qual foi o maior e o menor valor 
# digitado e as suas respectivas posições na lista. 

numeros = []
for i in range (5):
    numeros.append(int(input(f"Digite o {i+1}º valor: ")))
maior_numero = max(numeros)
menor_numero = min(numeros)
print(f"O maior número informado foi o: {maior_numero}")
print(f"O menor número informado foi o: {menor_numero}")
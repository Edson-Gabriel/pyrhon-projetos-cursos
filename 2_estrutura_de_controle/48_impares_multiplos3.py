# Faça um programa que mostre os números que são 
# impares e multiplos de 3 no intervalo de 1 - 500

soma = 0
contador = 0
for i in range (1, 500):
    if i % 2 == 1:
        print(i)
        if i % 3 == 0:
            contador += 1
            soma += i
print(soma)
print(contador)
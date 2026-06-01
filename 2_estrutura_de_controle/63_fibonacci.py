# Escreva um programa que leia um número N inteiro qualquer e 
# mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. 

valor1 = 0
valor2 = 1
sequencia = int(input('Digite até qual sequência de Fibonacci você quer ver: '))
contador = 0
while contador < sequencia:
    print(valor1, end=' | ')
    valor3 = valor1 + valor2
    valor1 = valor2
    valor2 = valor3
    contador += 1
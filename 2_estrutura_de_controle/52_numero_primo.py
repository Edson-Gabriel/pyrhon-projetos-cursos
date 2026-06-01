# Faça um programa que mostre se é número primo ou não

numero = int(input("Informe o número que você deseja saber se é primo ou não: "))
total = 0
for i in range (1, numero +1):
    if numero % i == 0:
        print("\033[33m", end='')
        total += 1
    else:
        print("\033[31m", end='')
    print(f'{i}', end= '')
print(f'\nO numero {numero} foi divisivel {total} vezes')
if total == 2:
    print('Por isso ele É PRIMO!')
else:
    print('Por isso ele NÃO É PRIMO!')
# Faça um programa que tenha uma função chamada maior(), que 
# receba vários parâmetros com valores inteiros. Seu programa 
# tem que analisar todos os valores e dizer qual deles é o maior.

from time import sleep

def maior(*num):
    sleep(0.5)
    print("-="*50)
    print("Analisando os valores informados...")
    if len(num) > 0:
        numero_maior = max(num)
        for valor in num:
            print(f"{valor}", end=", ", flush=True)
            sleep(0.3)
    else:
        numero_maior = 0
    print(f"Foram informados {len(num)} valores ao todo.")
    print(f"O maior número informado foi o {numero_maior}")

while True:
    numeros_informados_str = input('Informe os números que você deseja ver separado por "," (vírgulas): ')
    if len(numeros_informados_str) > 0:
        numeros_int = [int(n.strip()) for n in numeros_informados_str.split(",")]
    else:
        numeros_int = []
    maior(*numeros_int)
    while True:
        opcao = input("Quer continuar? [S/N] ").strip().upper()[0]
        if opcao not in "SN":
            print('Digite somente "SIM" ou "NÃO"!')
        else:
            break
    if opcao in "N":
        break
print("FIM")
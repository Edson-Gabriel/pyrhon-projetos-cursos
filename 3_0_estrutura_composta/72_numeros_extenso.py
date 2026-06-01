# Crie um programa que tenha uma dupla totalmente preenchida com 
# uma contagem por extenso, de zero até vinte. Seu programa deverá 
# ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

tupla_extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 
                 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    while True:
        print('='*30)
        tupla = int(input("Informe qual número de 0-20 você quer ver por extenso: "))
        if 0 <= tupla <=20:
            break
        print("="*30)
        print("Tente novamente com um número de 0 - 20...")
    print(f"O número digitado é o {tupla_extenso[tupla]}")
    while True:
        opcao = input("Quer continuar? [S/N] ").strip().upper()[0]
        if opcao in "SN":
            break
    if opcao == "N":
        break
print("Obrigado")
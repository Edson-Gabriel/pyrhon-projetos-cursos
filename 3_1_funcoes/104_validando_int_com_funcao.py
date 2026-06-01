# Crie um programa que tenha a função leiaInt(), que vai 
# funcionar de forma semelhante 'a função input() do Python, 
# só que fazendo a validação para aceitar apenas um valor 
# numérico.

def leia_int(msg):
    valor = 0
    ok = False
    while True:
        n = input(msg)
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print("\033[0;31mDIGITE UM NÚMERO INTEIRO VÁLIDO.\033[m") #cor vermelha
        if ok:
            return valor


n = leia_int("Digite um número: ")
print(f"Você acabou de digitar o número {n}")

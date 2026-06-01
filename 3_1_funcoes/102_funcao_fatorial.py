# Crie um programa que tenha uma função fatorial() que 
# receba dois parâmetros: o primeiro que indique o número 
# a calcular e outro chamado show, que será um valor 
# lógico (opcional) indicando se será mostrado ou não na 
# tela o processo de cálculo do fatorial.

def fatorial(num, show=False):
    """FUNÇÃO FATORIAL

    Args:
        num integer: Número que quer ver o fatorial
        show (bool, optional): Informar se quer ver o cálculo. Defaults to False.
        return: O valor do fatorial de um número (num)
    """
    f = 1
    for i in range(num, 0, -1):
        if show:
            print(i, end="")
            print(" x " if i > 1 else " = ", end="")
        f *= i
    return f


numero_fatorial = int(input("Fatorial de: "))
opcao = input("Deseja ver a conta? [S/N] ").strip().upper()[0]
if opcao not in "SN":
    print("ERRO! Não entendi!")
elif opcao in "S":
    print(fatorial(numero_fatorial, show=True))
else:
    print(fatorial(numero_fatorial))
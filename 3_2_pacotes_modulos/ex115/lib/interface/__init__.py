from lib.cores import*

def leia_inteiro(msg):
    while True:
        try:
            n_int = int(input(msg))
            return n_int
        except (ValueError, TypeError):
            print("ERRO: por favor, digite um número inteiro")
        except KeyboardInterrupt:
            print("PROGRAMA INTERROMPIDO PELO USUÁRIO!")
            return 0
        
def linha (tam=42):
    print("-"*tam)

def cabecalho(msg):
    linha()
    print(msg.center(42))
    linha()

def menu(lista=[]):
    cabecalho("MENU PRINCIPAL")
    for i, item in enumerate(lista):
        print(colorir(f"{i+1} -".ljust(10), "amarelo"), colorir(f"{item}".rjust(30), "azul"))
    linha()
    opcao = leia_inteiro(colorir("Sua opção: ","amarelo"))
    return opcao
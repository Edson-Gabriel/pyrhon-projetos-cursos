def leia_inteiro(n_int=0):
    while True:
        try:
            n_int = int(input("Digite um número inteiro: "))
            return n_int
        except (ValueError, TypeError):
            print("ERRO: por favor, digite um número inteiro")
        except KeyboardInterrupt:
            print("PROGRAMA INTERROMPIDO PELO USUÁRIO!")
            return n_int
            

def leia_real(n_float=0):
    while True:
        try:
            n_float = float(input("Digite um número real: "))
            return n_float
        except (ValueError, TypeError):
            print("ERRO: por favor, digite um número real")
        except KeyboardInterrupt:
            print("PROGRAMA INTERROMPIDO PELO USUÁRIO!")
            return n_float
            
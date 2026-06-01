from lib.interface import cabecalho
def arquivoExiste(nome):
    try:
        a = open(nome, "rt")
        a.close()
        return True
    except FileNotFoundError:
        return False
    
def criar_arquivo(nome):
    try:
        a = open(nome, "wt+")
        a.close()
        print(f"Arquivo {nome} criado com sucesso!")
    except:
        print("ERRO na criação!")

def ler_arquivo(nome):
    try:
        a = open(nome, "rt")
        cabecalho("PESSOAS CADASTRADAS")
        print("NOME".ljust(30), "IDADE".rjust(12))
        for linha in a:
            dado = linha.split(";")
            dado[1]=dado[1].replace("\n","")
            print(f"{dado[0]:<30}{dado[1]:>8} anos")
    except:
        print("Houve um erro durante a leitura do arquivo!")
    finally:
        a.close()

def cadastro_novo(arq, nome="Desconhecido", idade=0):
    try:
        a = open(arq, "at")
        try:
            a.write(f"{nome};{idade}\n")
            print(f"Novo registro do(a) {nome} adicionado!")
            a.close()
        except:
            print("Houve um erro durante o novo registro.")
    except:
        print("Houve um erro na abertura do arquivo!")
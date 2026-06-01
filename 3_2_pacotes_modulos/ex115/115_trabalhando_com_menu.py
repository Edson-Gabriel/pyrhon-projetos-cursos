# Criando um menu com interação

from lib.cores import*
from lib.interface import*
from lib.files import*
from time import sleep
arquivo = "dadosImportantes.txt"

if not arquivoExiste(arquivo):
    criar_arquivo(arquivo)

while True:
    resposta = menu(["Listar Usuários", "Cadastrar Usuário", "Sair do Sistema"])
    if resposta == 1:
        # cabecalho("Opção 1")
        ler_arquivo(arquivo)
    elif resposta == 2:
        cabecalho("NOVO CADASTRO")
        nome = str(input("Nome: "))
        idade = leia_inteiro('Idade: ')
        cadastro_novo(arquivo, nome, idade)
    elif resposta == 3:
        cabecalho("Opção 3")
        break
    else:
        cabecalho(colorir("Opcao Inválida!", "vermelho"))
    sleep(2)
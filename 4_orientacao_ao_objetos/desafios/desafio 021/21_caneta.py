# Escrevendo usando cores.

from rich import print

class Caneta:
    def __init__(self, cor = "azul"):
        escolha = ""
        match cor.lower().strip():
            case "azul":
                escolha = "[blue]"
            case "vermelho":
                escolha = "[red]"
            case "verde":
                escolha = "[green]"
            case _:
                escolha = "[white]"
        self.cor = escolha
        self.tampada = True

    def escrever(self, msg):
        if self.tampada:
            print(f":prohibited: A {self.cor}caneta[/] está tampada!")
        else:
            print(f"{self.cor}{msg}[/]", end=' ')

    def quebrar_linha(self, qtd = 1):
        print("\n" * qtd, end=' ')
    
    def tampar(self):
        self.tampada = True

    def destampar(self):
        self.tampada = False


caneta_1 = Caneta("azul")
caneta_2 = Caneta("vermelho")
caneta_3 = Caneta("verde")
caneta_4 = Caneta("")

caneta_1.destampar()
caneta_2.destampar()
caneta_3.destampar()
caneta_4.destampar()

caneta_1.escrever("Olá, Mundo!")
caneta_2.escrever("Funciona?!")
caneta_2.quebrar_linha(3)
caneta_3.escrever("Teste...")
caneta_4.escrever("Explosion")
caneta_4.quebrar_linha(5)

caneta_1.tampar()
caneta_1.escrever("Agora vai??")
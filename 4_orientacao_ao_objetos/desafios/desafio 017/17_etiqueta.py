# Criando uma etiqueta

from rich import print
from rich.panel import Panel
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def __str__(self):
        return f"{self.nome} custa R${self.preco:,.2f}"
    
    def etiqueta(self):
        conteudo = f"{self.nome.center(30, ' ')}"
        conteudo += f"{'-'*30}"
        precof = f"R${self.preco:,.2f}"
        conteudo += f"{precof.center(30, '.')}"
        etiqueta = Panel(conteudo, title="Produto", width=34)
        print(etiqueta)


produto_1 = Produto("S23", 2000)
produto_2 = Produto("Mesa de sinuca", 4500)
produto_1.etiqueta()
produto_2.etiqueta()
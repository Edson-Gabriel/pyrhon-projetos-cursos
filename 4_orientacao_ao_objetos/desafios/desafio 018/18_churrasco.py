# Analisando gastos para um churrasco

from rich import print
class Churrasco:
    consumo_padrao = 0.4
    preco_kg = 82.40

    def __init__(self, titulo = "Churrasco dos Amigos", convidados = 0):
        self.titulo = titulo
        self.quantidade = convidados
    
    def analisar(self):
        consumo_previsto = Churrasco.consumo_padrao * self.quantidade
        preco_final_total = Churrasco.preco_kg * consumo_previsto
        preco_final_pessoa = preco_final_total / self.quantidade
        print(f"Analisando [green]{self.titulo}[/] com [blue]{self.quantidade} convidados[/].\nCada participante comerá {Churrasco.consumo_padrao}Kg e cada Kg custa R${Churrasco.preco_kg}")
        print(f"Recomendo [blue]comprar {consumo_previsto:.3f}Kg[/] de carne.\nO custo total será de [green]R${preco_final_total:.2f}[/]")
        print(f"Cada pessoa pagará [yellow]R${preco_final_pessoa:.2f}[/] para participar")

resenha = Churrasco(convidados=15)
resenha.analisar()
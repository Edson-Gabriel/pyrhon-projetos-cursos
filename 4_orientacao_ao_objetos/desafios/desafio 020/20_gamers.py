# Criando um perfil gamer
class Gamer:
    def __init__(self, nome, nick):
        self.nome = nome
        self.nick = nick
        self.favoritos = []

    def add_favorites(self, jogo):
        self.favoritos.append(jogo)
        self.favoritos = sorted(self.favoritos)

    def ficha(self):
        print(f"Nome: {self.nome}")
        print(f"Nick: {self.nick}")
        for indice, game in enumerate(self.favoritos):
            print(game)

j1 = Gamer("Gabriel", "GabeSH")
j1.add_favorites("Valorant")
j1.add_favorites("Counter Stricke")
j1.add_favorites("Efootball")
j1.ficha()
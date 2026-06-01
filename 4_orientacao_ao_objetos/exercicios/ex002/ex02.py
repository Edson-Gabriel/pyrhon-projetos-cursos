class Gafanhoto:
    def __init__(self, nome= "", idade=0): #metodo construtor
        #Atributo de instancia
        self.nome = nome
        self.idade = idade

    #Método de instancias
    def aniversario(self):
        self.idade += 1

    def mensagem(self):
        return f"{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade."
    

g1 = Gafanhoto("Gabriel", 22)
g1.aniversario()
print(g1.mensagem())
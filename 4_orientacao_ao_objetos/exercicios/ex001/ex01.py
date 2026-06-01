class Gafanhoto:
    def __init__(self): #metodo construtor
        #Atributo de instancia
        self.nome = ""
        self.idade = 0

    #Método de instancias
    def aniversario(self):
        self.idade += 1

    def mensagem(self):
        return f"{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade."
    

g1 = Gafanhoto()
g1.nome = "Gabriel"
g1.idade = 22
g1.aniversario()
print(g1.mensagem())
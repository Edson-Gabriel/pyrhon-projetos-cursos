# Fazendo uma apresentação

class Funcionario():
    empresa = "Code By GB"
    def __init__(self, nome, setor, cargo):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo
    
    def apresentar(self):
        return f"Olá, me chamo {self.nome}, sou do setor {self.setor} e estou no cargo de {self.cargo} na empresa {Funcionario.empresa}"
    

colaborador_1 = Funcionario("Gabriel", "TI", "Programador")
print(colaborador_1.apresentar())
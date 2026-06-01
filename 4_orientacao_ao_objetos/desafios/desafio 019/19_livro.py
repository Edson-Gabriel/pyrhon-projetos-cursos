# Marca páginas

class Livro:
    def __init__(self, titulo, paginas):
        self.titulo = titulo
        self.total_paginas = paginas
        self.pagina_atual = 1

        print(f"Você acabou de abrir o livro que tem {self.total_paginas} paginas no total. Você agora esta na pagina {self.pagina_atual}!")

    def avancar_paginas(self, qtd = 1):
        cont = 0 
        for pg in range (0, qtd, 1):
            if not self.fim_do_livro():
                self.pagina_atual += 1
                print(f"Pág {self.pagina_atual} ->", end=' ')
                cont += 1
        print(f"Você avançou {cont} páginas e agora esta na pagina {self.pagina_atual}!")
        if self.fim_do_livro():
            print(f"Você chegou ao final do livro '{self.titulo}'")

    def fim_do_livro(self) -> bool:
        return True if self.pagina_atual == self.total_paginas else False
        

livro_1 = Livro("Tentando aprender", 25)
livro_1.avancar_paginas(4)
livro_1.avancar_paginas(15)
livro_1.avancar_paginas(3)
livro_1.avancar_paginas(1)
livro_1.avancar_paginas(4)
livro_1.avancar_paginas(1)
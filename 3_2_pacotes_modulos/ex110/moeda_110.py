def aumentar(valor=0, taxa=0, formatado=False):
    aumento = valor+(valor*(taxa/100))
    return aumento if formatado is False else moeda(aumento)


def diminuir(valor=0, taxa=0, formatado=False):
    diminuindo = valor-(valor*(taxa/100))
    return diminuindo if formatado is False else moeda(diminuindo)


def dobrando(valor=0, formatado=False):
    dobro = valor*2
    return dobro if formatado is False else moeda(dobro)


def metade(valor=0, formatado=False):
    metade = valor/2
    return metade if formatado is False else moeda(metade)

def moeda(valor=0, moeda="R$"):
    return f"{moeda}{valor:.2f}".replace(".", ",")

def resumo(valor=0, taxa_aumento=10, taxa_reducao = 15):
    print("-"*40)
    print("RESUMO DO VALOR".center(40))
    print("-"*40)
    print(f"Preco analisado".ljust(20), f"{moeda(valor)}".rjust(20))
    print(f"Dobro do preço:".ljust(20), f"{dobrando(valor, True)}".rjust(20))
    print(f"Metade do preço:".ljust(20), f"{metade(valor, True)}".rjust(20))
    print(f"{taxa_aumento}% de aumento:".ljust(20), f"{aumentar(valor, taxa_aumento, True)}".rjust(20))
    print(f"{taxa_reducao}% de redução:".ljust(20), f"{diminuir(valor, taxa_reducao, True)}".rjust(20))


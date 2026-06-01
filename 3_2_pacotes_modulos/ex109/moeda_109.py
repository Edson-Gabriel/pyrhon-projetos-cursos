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
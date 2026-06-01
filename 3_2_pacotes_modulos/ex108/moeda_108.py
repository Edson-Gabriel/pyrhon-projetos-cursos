def aumentar(p, taxa):
    aumento = p+(p*(taxa/100))
    return aumento


def diminuir(p, taxa):
    diminuindo = p-(p*(taxa/100))
    return diminuindo


def dobrando(valor=0):
    dobro = valor*2
    return dobro


def metade(valor=0):
    metade = valor/2
    return metade

def moeda(valor=0, moeda="R$"):
    return f"{moeda}{valor:.2f}".replace(".", ",")
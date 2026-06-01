def aumentar(valor=0, taxa=0, formatado=False):
    """_summary_

    Args:
        valor (int, optional): Valor da moeda que o usuário deve informar. Defaults to 0.
        taxa (int, optional): informar a taxa de aumento. Defaults to 0.
        formatado (bool, optional): Se o usuário quer ver a formatação estilizada com o "R$". Defaults to False.

    Returns:
        float: Retorna o valor já calculando o acréscimo da taxa.
    """

    aumento = valor+(valor*(taxa/100))
    return aumento if formatado is False else moeda(aumento)


def diminuir(valor=0, taxa=0, formatado=False):

    """_summary_

    Args:
        valor (int, optional): Valor da moeda que o usuário deve informar. Defaults to 0.
        taxa (int, optional): informar a taxa de desconto. Defaults to 0.
        formatado (bool, optional): Se o usuário quer ver a formatação estilizada com o "R$". Defaults to False.

    Returns:
        float: Retorna o valor já calculando o desconto da taxa.
    """

    diminuindo = valor-(valor*(taxa/100))
    return diminuindo if formatado is False else moeda(diminuindo)


def dobrando(valor=0, formatado=False):
    """_summary_

    Args:
        valor (int, optional): Valor da moeda que o usuário deve informar. Defaults to 0.
        formatado (bool, optional): Se o usuário quer ver a formatação estilizada com o "R$". Defaults to False.

    Returns:
        float: retorna o dobro do valor informado.
    """
    
    dobro = valor*2
    return dobro if formatado is False else moeda(dobro)


def metade(valor=0, formatado=False):

    """_summary_

    Args:
        valor (int, optional): Valor da moeda que o usuário deve informar. Defaults to 0.
        formatado (bool, optional): Se o usuário quer ver a formatação estilizada com o "R$". Defaults to False.

    Returns:
        float: retorna a metade do valor informado.
    """

    metade = valor/2
    return metade if formatado is False else moeda(metade)

def moeda(valor=0, moeda="R$"):
    """_summary_

    Args:
        valor (int, optional): Se o usuário quer ver a formatação estilizada com o "R$". Defaults to 0.
        moeda (str, optional): Qual a moeda que o usuário deseja ver ("R$", "$", "€"). Defaults to "R$".

    Returns:
        _type_: Retorna estilizado para o usuário, com o cifrão escolhido acompanhado do valor.
    """
    
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


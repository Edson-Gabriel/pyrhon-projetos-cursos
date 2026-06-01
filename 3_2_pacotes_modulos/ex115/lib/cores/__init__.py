def colorir(texto, cor="reset"):
    cores = {
        "reset": "\033[0m",
        "vermelho": "\033[31m",
        "verde": "\033[32m",
        "amarelo": "\033[33m",
        "azul": "\033[34m",
        "roxo": "\033[35m",
        "ciano": "\033[36m",
        "branco": "\033[37m",
        "negrito": "\033[1m"
    }
    
    # Busca a cor no dicionário ou volta para o padrão (reset)
    codigo = cores.get(cor.lower(), cores["reset"])
    
    return f"{codigo}{texto}{cores['reset']}"
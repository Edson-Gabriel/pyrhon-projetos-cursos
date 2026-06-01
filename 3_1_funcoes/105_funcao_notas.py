# Faça um programa que tenha uma função notas() que pode receber 
# várias notas de alunos e vai retornar um dicionário com as 
# seguintes informações:

# Quantidade de notas
# A maior nota
# A menor nota
# A média da turma
# A situação (opcional)

# Adicione também as docstrings dessa função para consulta pelo 
# desenvolvedor.

def notas(*valores, sit = False):
    """NOTAS

    Args:
        valores: aceita diversos valores (notas) que se baseia o dicionário 
        sit (bool, optional): Mostra a situação do aluno. Defaults to False.

    Returns:
        dicionario com as informações dos alunos
    """

    total = len(valores)
    media = sum(valores)/total if total > 0 else 0
    notas= {
        'total' : total,
        'maior' : max(valores) if total > 0 else 0,
        'menor' : min(valores) if total > 0 else 0,
        'media' : media
    }
    if sit:
        if media < 5.5:
            notas['situacao'] = "Reprovado"
        elif media < 7.5:
            notas['situacao'] = "Recuperação"
        elif media <= 10:
            notas['situacao'] = "Aprovado"
    return notas


print(notas(5, 7, 9, 10, sit=True))

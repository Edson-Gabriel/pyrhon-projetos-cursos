# Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, 
# mostrando os 10 primeiros termos da progressão usando a estrutura while
primeiro_termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
contagem = 0

while contagem < 10:
    termo = razao * contagem + primeiro_termo
    print(f"{termo}", end=" → ")
    contagem += 1

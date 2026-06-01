# Crie um programa onde o usuário possa digitar cinco valores 
# numéricos e cadastre-os em uma lista, já na posição correta 
# de inserção (sem usar o sort()). No final, mostre a lista 
# ordenada na tela.

lista_completa = []
for i in range(5):
    numero_novo = int(input(f"Digite um valor: "))
    if i == 0 or numero_novo > lista_completa[-1]:
        lista_completa.append(numero_novo)
        print("Adicionado na última posição!")
    else:
        posicao = 0
        while posicao < len(lista_completa):
            if numero_novo < lista_completa[posicao]:
                lista_completa.insert(posicao, numero_novo)
                print(f"Foi adicionado na posição {posicao}")
                break
            posicao += 1
print(f"A lista em ordem: {lista_completa}")
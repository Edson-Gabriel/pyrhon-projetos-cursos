# Crie um programa que tenha uma tupla única com nomes 
# de produtos e seus respectivos preços, na sequência. 
# No final, mostre uma listagem de preços, organizando 
# os dados em forma tabular.
produtos = "Café", 20.5, "Leite", 5.5, "Pão KG", 26.99
print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 40)
for i in range(0, len(produtos)):
    if i % 2 == 0:
        print(f"{produtos[i]:.<30}", end=" ")
    else:
        print(f"R${produtos[i]:>7.2f}")
        
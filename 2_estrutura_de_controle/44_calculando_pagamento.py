# Faça um programa que com base na forma de pagamento selecionado 
# mostre como ficou o valor final da venda.

preco_produto = 100
print('''
      1 - Dinheiro/Cheque (A VISTA)
      2 - Cartão (A VISTA)
      3 - Cartão (2x)
      4 - Cartão (3x ou mais)
''')
forma_de_pagamento = int(input("Informe a forma de pagamento: "))
if forma_de_pagamento == 1:
    preco_produto = preco_produto - (preco_produto * 0.1)
    print(f"O preço final do produto com desconto: R${preco_produto:.2f}")
elif forma_de_pagamento == 2:
    preco_produto = preco_produto - (preco_produto * 0.05)
    print(f"O preço final do produto com desconto: R${preco_produto:.2f}")
elif forma_de_pagamento == 3:
    print(f"O preço final do produto sem desconto: R${preco_produto:.2f}")
elif forma_de_pagamento == 4:
    preco_produto = preco_produto + (preco_produto * 0.2)
    print(f"O preço final do produto com juros: R${preco_produto:.2f}")
else:
    print("Forma de pagamento inválido")
# Escreva um programa para aprovar o empréstimo bancário para a
# compra de uma casa. Pergunte o valor da casa, o salário do 
# comprador e em quantos anos ele vai pagar. A prestação mensal
# não pode exceder 30% do salário ou então o empréstimo será negado.

valor_casa = float(input("Informe o valor da casa: R$"))
salario = float(input("Informe o valor do seu salario: R$"))
anos_pagando =  int(input("Informe em quantos anos pretende pagar: "))
valor_prestacao = valor_casa / (anos_pagando*12)
prestacao_minima = salario*0.3
if valor_prestacao <= prestacao_minima:
    print(f"Crédito aprovado com parcelas de R${valor_prestacao:.2f}. Sendo parcelas inferior a 30% do seu salario (R${salario:.2f})")
else:
    print(f"Crédito negado com parcelas de R${valor_prestacao:.2f}. Sendo parcelas superior a 30% do seu salario (R${salario:.2f})")
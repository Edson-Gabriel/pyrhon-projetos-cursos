# Crie um pacote chamado utilidadesCeV que tenha dois 
# módulos internos chamados moeda e dado. Transfira 
# todas as funções utilizadas nos desafios 107, 108 e 
# 109 para o primeiro pacote e mantenha tudo funcionando.

from utilidades_moedas import moedas

preco = float(input("Digite o preço: R$"))
moedas.resumo(preco, 20, 40)
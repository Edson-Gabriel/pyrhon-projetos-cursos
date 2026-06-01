# Faça um programa que calcule o aluguel de um carro
# R$60,00 por dia e R$0,15 por KM rodado

dias_total = int(input("Quantos dias ficou com o carro? "))
km_total = float(input("Quantos KM rodou no total? "))
km_valor = km_total * 0.15
dias_valor = dias_total * 60
valor_final = km_valor + dias_valor
print(f"Você rodou com o carro por {dias_total} dias e o percurso total foi de {km_total}km")
print(f"Preço pelos dias: R${dias_valor:.2f}. Preço pelos km percorrido {km_valor:.2f}")
print(f"O valor a ser pago de tudo no total de R${valor_final:.2f}")

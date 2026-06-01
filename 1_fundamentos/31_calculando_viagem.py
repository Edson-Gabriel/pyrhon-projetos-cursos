# Faça um programa que calcule os custo de viagem


# Feito com operador ternário
distancia = float(input("Sua viagem é de quantos KM? "))
custo_viagem = distancia * 0.5 if distancia <=200 else distancia * 0.45
print(f"Sua viagem de {distancia:.2f}KM vai ficar por R${custo_viagem:.2f}")

# Feito sem operador ternário
# distancia = float(input("Sua viagem é de quantos KM? "))
# if distancia <= 200:
#     custo_viagem = distancia * 0.5
#     print(f"Sua viagem é de {distancia:.2f}, cobramos R$0,50 por KM em distâncias de até 200KM. O valor final da sua viagem ficou de R${custo_viagem:.2f}")
# else:
#     custo_viagem = distancia * 4.45
#     print(f"Sua viagem é de {distancia:.2f}, cobramos R$0,45 por KM em distâncias com mais de 200KM. O valor final da sua viagem ficou de R${custo_viagem:.2f}")
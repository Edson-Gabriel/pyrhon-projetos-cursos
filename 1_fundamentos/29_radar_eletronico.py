# Validando se o condutor passou acima do limite permitido no radar.

velocidade_carro = float(input("Informe a velocidade do veículo (KM): "))
if velocidade_carro > 80:
    multa = (velocidade_carro - 80) * 7
    print(f"Você estava a {velocidade_carro:.2f}KM/h, {velocidade_carro - 80:.2f}KM/h. Sua multa ficou em R${multa:.2f}")
else:
    print(f"Liberado. Você estava a {velocidade_carro:.2f}KM/h.")
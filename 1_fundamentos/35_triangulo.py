# Validando se os valores informados formam ou não 1 triângulo

lado_a = int(input('Digite o lado "A" (maior lado) do possível triângulo: '))
lado_b = int(input('Digite o lado "B" do possível triângulo: '))
lado_c = int(input('Digite o lado "C" do possível triângulo: '))
if lado_a+lado_c > lado_b and lado_b+lado_c > lado_a:
    print('É um triângulo')
else:
    print('Não é triângulo')
print('FIM')
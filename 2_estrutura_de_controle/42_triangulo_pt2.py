# Validando se os valores informados formam ou não um triângulo

'''
Objetivo: Mostrar qual tipo de triângulo vai formar ou se não é um triângulo
Entrada: lados a, b e c 
Processamento: Verificar as condições para formar um triângulo.
Saída: Mostrar se é um triângulo equlátero, isóceles, escaleno ou se não forma o triângulo. 
'''

lado_a = int(input('Digite o lado "A" (maior lado) do possível triângulo: '))
lado_b = int(input('Digite o lado "B" do possível triângulo: '))
lado_c = int(input('Digite o lado "C" do possível triângulo: '))
if lado_a + lado_c > lado_b and lado_b+lado_c > lado_a:
    if lado_a == lado_b and lado_a == lado_c:
        print(f"É um triângulo equilátero")
    elif lado_a == lado_b or lado_a == lado_c or lado_b == lado_c:
        print(f"É um triângulo isóceles")
    else:
        print(f"É um triângulo escaleno")
else:
    print('Não é triângulo')
print('FIM')
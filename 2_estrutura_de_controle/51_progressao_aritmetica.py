# Progressão aritmética

primeiro_termo = int(input("Escolha o primeiro termo: "))
razao = int(input("Informe a razão escolhida: "))
for i in range (10):
    termo = razao * i + primeiro_termo
    print(termo)
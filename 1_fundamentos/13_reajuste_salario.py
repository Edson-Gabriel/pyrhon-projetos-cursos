# Faça um programa simulando um reajuste salarial de 15%

salario_antigo = float(input("Digite qual o seu antigo salário: R$"))
salario_atual = salario_antigo + (salario_antigo * 0.15)
print(f"Seu salário antigo era de R${salario_antigo:.2f} e seu salário atual com o reajuste é de R${salario_atual:.2f}")
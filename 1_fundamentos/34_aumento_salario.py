# Calulando aumento de salário com estrutura condicionais

salario_informado = float(input("Informe o seu salário: R$"))
if salario_informado > 1250.00:
    salario_atual = salario_informado + (salario_informado*0.10)
else:
    salario_atual = salario_informado + (salario_informado*0.15)
print(f"Seu salário era de R${salario_informado:.2f} com aumento foi para {salario_atual:.2f}")
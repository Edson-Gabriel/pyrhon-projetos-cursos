# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato. 

contador_produto = valor_venda_total = preco_maior_1000 = preco_barato = 0
while True:
    contador_produto += 1
    nome_produto = input(f"Informe o {contador_produto}º produto: ")
    preco_produto = float(input(f"Qual o valor desse {contador_produto}º: R$"))
    valor_venda_total += preco_produto

    if preco_produto > 1000:
        preco_maior_1000 += 1
    if contador_produto == 1 or preco_produto < preco_barato:
        preco_barato = preco_produto
        nome_barato = nome_produto
        
    opcao = " "
    while opcao not in "SsNn":
        opcao = input("Deseja continuar [S/N]: ").strip().upper()[0]
    if opcao == "N":
        break
print(f"\nO total gasto na compra foi de R${valor_venda_total:.2f}")
print(f"{preco_maior_1000} produtos custam mais de R$1000,00")
print(f"O produto mais barato é o {nome_barato}, que custa R${preco_barato:.2f}")
# Convertendo um número para binario, octal e hexadecimal

numero_base = int(input("Digite o número que deseja converter: "))
opcao = int(input("Digite opção desejada (1 BINÁRIO, 2 OCTAL, 3 HEXADECIMAL): "))
if opcao == 1:
    print(f"O número {numero_base} > Binário = {bin(numero_base)[2:]}")
elif opcao == 2:
    print(f"O número {numero_base} > Octal = {oct(numero_base)[2:]}")
elif opcao == 3:
    print(f"O número {numero_base} > Hexadecimal = {hex(numero_base)[2:]}")
else:
    print("Opção inválida!")
print("OBRIGADO POR UTILIZAR NOSSOS SERVIÇOS!!!")
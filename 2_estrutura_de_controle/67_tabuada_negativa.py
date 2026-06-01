# Faça um programa que mostre a tabuada de vários números, um de 
# cada vez, para cada valor digitado pelo usuário. O programa será 
# interrompido quando o número solicitado for negativo. 

while True:
    numero = int(input("Digite o numero que voce quer saber da tabuada: "))
    if numero < 0:
        break
    for num_2 in range(11):
        resultado = numero * num_2
        print(f"{numero} X {num_2:2} = {resultado}")
print("Acabou!")
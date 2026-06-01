# Faça um programa que leia algo pelo teclado e mostre na tela o 
# seu tipo primitivo e todas as informações possíveis sobre ele.

texto = (input("Digite algo: "))
print(f"O tipo primitivo desse valor é {type(texto)}")
print(f"Só tem espaço {texto.isspace()}")
print(f"É só número {texto.isnumeric()}")
print(f"É só letra {texto.isalpha()}")
print(f"É alphanúmerico {texto.isalnum()}")
print(f"Está em maiúsculo {texto.isupper()}")
print(f"Está em minúsculo {texto.islower()}")
print(f"Está capitalizada {texto.istitle()}")

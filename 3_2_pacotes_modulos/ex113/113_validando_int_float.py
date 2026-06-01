# Reescreva a função leiaInt() que fizemos no desafio 104, 
# incluindo agora a possibilidade da digitação de um número 
# de tipo inválido. Aproveite e crie também uma função 
# leiaFloat() com a mesma funcionalidade.

from validadores_uteis import numeros

num_int = numeros.leia_inteiro()
num_float = numeros.leia_real()
print(f"Número inteiro informado {num_int} e real {num_float}")
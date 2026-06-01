# Crie um programa onde o usuário digite uma expressão qualquer 
# que use parênteses. Seu aplicativo deverá analisar se a 
# expressão passada está com os parênteses abertos e fechados 
# na ordem correta.

expressao = str(input("Digite sua expressão: "))
validador = []
for simbolos in expressao:
    if simbolos == "(":
        validador.append("(")
    elif simbolos == ")":
        if len(validador) > 0:
            validador.pop()
        else:
            validador.append(")")
            break

if len(validador) == 0:
    print("Expressão válida!")
else:
    print("Expressão inválida!")
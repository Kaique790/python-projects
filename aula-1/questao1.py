ope = input("Digite a operação (+,-,x,%): ")
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

def operacao(x, n1, n2):
    if x == '+':
        return n1 + n2
    elif x == '-':
        return n1 - n2
    elif x == 'x':
        return n1 * n2
    elif x == '%':
        return n1 / n2
    else:
        return False
    
res = operacao(ope, n1, n2)
if (res == False):
    print("Operador inválido")
else:
    print(f"O resultado da operação é: {res}")
def count (n1, n2):
    type = input("Digite um opreção: +, -, *, /.: ")
    match type:
        case "+":
            print(n1 + n2)
        case "*":
            print(n1 * n2)
        case "-":
            print(n1 - n2)
        case "/":
            print(n1 / n2)
        case _:
            print("Digite uma opreção válida")

n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))

count(n1, n2)

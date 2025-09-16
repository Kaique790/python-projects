def calc_gain(qtd_travel: int):
    result = qtd_travel * 14.80
    print(f"Você ganha {result} R$")

value = int(input("Digite um valor: "))

calc_gain(value)

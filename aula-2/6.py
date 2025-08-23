def calc_juros(value):
    new_value = value + (value * 20/100)
    print(f"O novo valor com juros é de {new_value}")

value = int(input("Digite um valor: "))

calc_juros(value)

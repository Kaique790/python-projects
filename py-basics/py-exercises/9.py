def calc_real_to_dol(value: int):
    usd_in_brl = 0.18
    result =  value * usd_in_brl
    print(f"{value} R$ é igual a {result}$")

value = int(input("Digite um valor: "))

calc_real_to_dol(value)

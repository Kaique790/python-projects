def calc_cel_to_fahre(c: int):
    f = (c * 9/5) + 32.
    print(f"{c} °C em Fahrenheit, é {f} °F")

c = int(input("Digite qtd. de graus celsius: "))

calc_cel_to_fahre(c)

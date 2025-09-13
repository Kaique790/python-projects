def calc_age(nome, ano_nasc):
    age = 2025 - ano_nasc
    print(f"{nome}, você tem {age}")


nome = input("Digite seu nome: ")
ano_nasc = int(input("Digite ano de nasc: "))

calc_age(nome, ano_nasc)

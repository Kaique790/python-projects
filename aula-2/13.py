def calc(age: int):
    if age < 16:
        print("não pode votar")
    elif age >= 16 and age <= 17 or age > 70:
        print("Voto opcional")
    else:
        print("Voto obrigatório")

age = int(input("Digite sua idade: "))

calc(age)

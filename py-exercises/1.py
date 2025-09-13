print("cores no semáforo: vermelho - verde - amarelo")
cor = input("Digite um cor: ")

if cor == "verde":
    print("continue")
elif cor == "vermelho":
    print("pare")
elif cor == "amarelo":
    print("Espere")
else:
    print("Digite uma cor válida")
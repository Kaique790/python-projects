deposited = float(input("Digite quanto quer depositar: "))

def validate_deposit_value(value):
    if value <= 0:
        print("Saque inválido")
        return False
    return True

valid = validate_deposit_value(deposited)

while True:
    if not valid: 
        continue

    saque = int(input("Digite quanto quer sacar: "))

    if saque == 0:
        print("Cancelando saque...")
        break

    if saque < 0:
        print("Digite um saque válido")
        continue

    if saque > 500:
        print("O saque não pode ser maior que 500...")
        continue

    if saque > deposited:
        print("Saldo insuficiente")
        continue

    deposited -= saque
    print(f"Você sacou {saque} R$.")
    print(f"Você tem {deposited} R$ disponível.")

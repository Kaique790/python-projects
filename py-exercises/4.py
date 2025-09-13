def calc_aprove(nome, horas_mes, horas_falta):
    if (horas_falta / horas_mes) > 0.25:
        print(f"{nome}, você reprovou por falta")
        print(f"Qtd. de falta: {horas_falta / horas_mes * 100}%")

nome = input("Digite seu nome")
horas_mes = float(input("Digite qdt. horas de letivas no mês: "))
horas_falta = float(input("Digite qdt. horas faltadas no mês: "))

calc_aprove(nome, horas_mes, horas_falta)

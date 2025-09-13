import pandas as pd

structure_table = {
    "tarefa": [],
    "situação": []
}

dataframe = pd.DataFrame(structure_table)
dataframe.to_excel("todo.xlsx")

while True:
    tasks = []

    task = input("Digite uma tarefa! (exit) para sair.")
    if task == "exit":
        print("Saindo...")
        exit

    tasks.append(task)
    



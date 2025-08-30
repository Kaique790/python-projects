import pandas as pd

structure_table = {
    "tarefa": [],
    "situação": []
}

dataframe = pd.DataFrame(structure_table)
dataframe.to_excel("todo.xlsx")


import pandas as pd

dataframe = pd.DataFrame

vendas_df = pd.read_excel('Vendas.xlsx')
vendas_df["Comissão"] = vendas_df["Valor Final"] * 0.05

vendas_dez_df = pd.read_excel('Vendas - Dez.xlsx')
vendas_df = pd.concat([vendas_df, vendas_dez_df])
vendas_df.loc[:, "Imposto"] = 0

# Deletar coluna
# vendas_df = vendas_df.drop("Imposto", axis=1) 
vendas_df = vendas_df.drop(columns="Imposto")

# Deletar linhas ou colunas totalmente vazias
vendas_df = vendas_df.dropna(how="all", axis=1)

# Deletar linhas com algum campo vazio
vendas_df = vendas_df.dropna()

print(vendas_df)
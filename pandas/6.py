import pandas as pd

dataframe = pd.DataFrame

vendas_df = pd.read_excel('Vendas.xlsx')
vendas_df["Comissão"] = vendas_df["Valor Final"] * 0.05

colunas = ["Produto", "Valor Final", "Comissão"]

# Agrupo colunas e somo as colunas que eu quiser
faturamento_produto = vendas_df[colunas].groupby("Produto")[colunas].sum()
print(faturamento_produto)